import logging
import time
import math
import base64
import requests
import os
from django.conf import settings

from datetime import datetime
from requests.auth import HTTPBasicAuth
from requests import Response

ENVIRONMENT = os.environ.get("MPESA_ENVIRONENT", "development")
CHECKOUT_URL = settings.MPESA_DEV_CHECKOUT_URL if ENVIRONMENT.lower() == "development" else settings.MPESA_PROD_CHECKOUT_URL
TOKEN_ACCESS_URL = settings.MPESA_ACCESS_DEV_TOKEN_URL if ENVIRONMENT.lower() == "development" else settings.MPESA_ACCESS_PROD_TOKEN_URL

#from mpesa_integration.settings import env
from .models import *
from .exceptions import *


logging = logging.getLogger("default")

now = datetime.now()


class MpesaResponse(Response):
	response_description = ""
	error_code = None
	error_message = ''


def mpesa_response(r):
	"""
	Create MpesaResponse object from requests.Response object
	
	Arguments:
		r (requests.Response) -- The response to convert
	"""

	r.__class__ = MpesaResponse
	json_response = r.json()
	r.response_description = json_response.get('ResponseDescription', '')
	r.error_code = json_response.get('errorCode')
	r.error_message = json_response.get('errorMessage', '')
	return r


class MpesaGateWay:
    business_shortcode = None
    consumer_key = None
    consumer_secret = None
    access_token_url = None
    access_token = None
    access_token_expiration = None
    checkout_url = None
    timestamp = None
    headers = None
    
    def __init__(self, business_shortcode, consumer_key, consumer_secret, callback_url, phone_number, amount, account_reference, transaction_desc, token):
        now = datetime.now()
        self.business_shortcode = business_shortcode
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token_url =  TOKEN_ACCESS_URL
        self.callback_url =callback_url
        self.phone_number = phone_number
        self.amount = amount
        self.account_reference = account_reference
        self.transaction_desc = transaction_desc
        self.token = token
        self.password = self.generate_password()
        #self.headers = {"Authorization": f"Bearer {self.token}"}
      
        self.checkout_url = CHECKOUT_URL

        try:
            self.access_token = self.getAccessToken()

            if self.access_token is None:
                raise Exception("Request for access token failed.")
        except Exception as e:
            logging.error("Error {}".format(e))
            # print("Hellen")
        else:
            self.access_token_expiration = time.time() + 340000000000000000

    def getAccessToken(self):
        """
        try:
            res = requests.get(self.access_token_url, auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret))
            print(res)
        except Exception as err:
            logging.error("Error {}".format(err))
            # raise err
        else:
            token = res.json()["access_token"]
            self.headers = {"Authorization": "Bearer %s" % token}
        """
        return self.token

    class Decorators:
        @staticmethod
        def refreshToken(decorated):
            def wrapper(gateway, *args, **kwargs):
                if (gateway.access_token_expiration and time.time() > gateway.access_token_expiration):
                    token = gateway.getAccessToken()
                    gateway.access_token = token
                return decorated(gateway, *args, **kwargs)

            return wrapper

    def generate_password(self):
        """Generates mpesa api password using the provided shortcode and passkey"""
        self.timestamp = now.strftime("%Y%m%d%H%M%S")
        password_str = settings.MPESA_SHORTCODE + settings.MPESA_PASSKEY + self.timestamp
        password_bytes = password_str.encode("ascii")
        return base64.b64encode(password_bytes).decode("utf-8")


    @Decorators.refreshToken
    def stk_push(self):
        if str(self.account_reference).strip() == '':
            raise MpesaInvalidParameterException('Account reference cannot be blank')
        if str(self.transaction_desc).strip() == '':
            raise MpesaInvalidParameterException('Transaction description cannot be blank')
        if not isinstance(self.amount, int):
            raise MpesaInvalidParameterException('Amount must be an integer')

        req_data = {
            "BusinessShortCode": self.business_shortcode,
            "Password": self.password,
            "Timestamp": self.timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": self.amount,
            "PartyA": self.phone_number,
            "PartyB": self.business_shortcode,
            "PhoneNumber": self.phone_number,
            "CallBackURL": self.callback_url,
            "AccountReference": self.account_reference,
            "TransactionDesc": self.transaction_desc,
        }

        print(req_data)

        try:
            res = requests.post(self.checkout_url, json=req_data, headers=self.headers, timeout=30)
            response = mpesa_response(res)
            return response
        except requests.exceptions.ConnectionError:
            raise MpesaConnectionError('Connection failed')
        except Exception as ex:
            raise MpesaConnectionError(str(ex))


    @Decorators.refreshToken
    def c2b(self, amount, phone_number, bill_reference_number):
        if str(bill_reference_number).strip() == '':
            raise MpesaInvalidParameterException('Bill reference cannot be blank')
        if str(phone_number).strip() == '':
            raise MpesaInvalidParameterException('Transaction description cannot be blank')
        if not isinstance(amount, int):
            raise MpesaInvalidParameterException('Amount must be an integer')

        req_data = {
            "CommandID": "CustomerPaybillOnline",
            "Amount": amount,
            "Msisdn": phone_number,
            "BillRefNumber": bill_reference_number,
            "ShortCode": self.business_shortcode
        }

        try:
            res = requests.post(self.checkout_url, json=req_data,
                                headers=self.headers, timeout=30)
            response = mpesa_response(res)

            return response
        except requests.exceptions.ConnectionError:
            raise MpesaConnectionError('Connection failed')
        except Exception as ex:
            raise MpesaConnectionError(str(ex))
