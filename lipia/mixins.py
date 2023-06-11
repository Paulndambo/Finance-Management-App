import os
from datetime import datetime, timedelta
import time
from lipia.utils import generate_payment_timestamps, get_mpesa_transaction_password
import requests
from requests.auth import HTTPBasicAuth
import json
import base64

from django.conf import settings
from lipia.models import ServiceProvider
from requests import Response
from .exceptions import *


ENVIRONMENT = os.environ.get("MPESA_ENVIRONENT")
CHECKOUT_URL = settings.MPESA_DEV_CHECKOUT_URL if ENVIRONMENT.lower() == "development" else settings.MPESA_PROD_CHECKOUT_URL
TOKEN_ACCESS_URL = settings.MPESA_ACCESS_DEV_TOKEN_URL if ENVIRONMENT.lower() == "development" else settings.MPESA_ACCESS_PROD_TOKEN_URL

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


class MpesaPaymentProcessingMixin(object):
    def __init__(self, business_shortcode, consumer_key, consumer_secret, callback_url, phone_number, amount, account_reference, transaction_desc):
        self.business_shortcode = business_shortcode
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.callback_url = callback_url
        self.phone_number = phone_number
        self.amount = amount
        self.account_reference = account_reference
        self.transaction_desc = transaction_desc
        self.access_token_expiration = time.time() + 340000000000000000
        self.password = self.__generate_password()

    def run(self):
        self.__generate_password()
        self.__authenticate_to_mpesa()
       

    def __authenticate_to_mpesa(self):
        response = requests.get(TOKEN_ACCESS_URL, auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret))
        token = json.loads(response.content)['access_token']

        return token
    
    def __generate_password(self):
        self.timestamp = now.strftime("%Y%m%d%H%M%S")
        password_str = self.business_shortcode + settings.MPESA_PASSKEY + self.timestamp
        password_bytes = password_str.encode("ascii")
        generated_password = base64.b64encode(password_bytes).decode("utf-8")
        return generated_password
    
    def process_stk_push_payment(self):
        if str(self.account_reference).strip() == '':
            raise MpesaInvalidParameterException('Account reference cannot be blank')
        if str(self.transaction_desc).strip() == '':
            raise MpesaInvalidParameterException('Transaction description cannot be blank')
        if not isinstance(self.amount, int):
            raise MpesaInvalidParameterException('Amount must be an integer')

        #phone_number = phone_number
        #business_shortcode = self.business_shortcode
        #timestamp = self.timestamp
        #password = self.password

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

    


        
