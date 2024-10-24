import logging
import time
import math
import base64
import requests

from datetime import datetime
from requests.auth import HTTPBasicAuth
from requests import Response

# from mpesa_integration.settings import env
from .models import *
from .exceptions import *
from django.conf import settings

logging = logging.getLogger("default")

now = datetime.now()


class MpesaResponse(Response):
    response_description = ""
    error_code = None
    error_message = ""


def mpesa_response(r):
    """
    Create MpesaResponse object from requests.Response object

    Arguments:
            r (requests.Response) -- The response to convert
    """

    r.__class__ = MpesaResponse
    json_response = r.json()
    r.response_description = json_response.get("ResponseDescription", "")
    r.error_code = json_response.get("errorCode")
    r.error_message = json_response.get("errorMessage", "")
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

    def __init__(self):
        now = datetime.now()
        self.business_shortcode = "174379"
        self.consumer_key = "b0rDIAymbVQa0wM8m1IDmqQZ4AeVaQIEBDeAyYRqFpOuHzeQ"
        self.consumer_secret = "nT9HygFAva4R60ThO55PwJMspyicEQZU2dWYHi8scFZlIJAMcTo2zqPSdRZanOXq"
        self.access_token_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
        self.password = self.generate_password()
        self.checkout_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

        try:
            self.access_token = self.getAccessToken()
            if self.access_token is None:
                raise Exception("Request for access token failed.")
        except Exception as e:
            logging.error("Error {}".format(e))
        else:
            self.access_token_expiration = time.time() + 340000000000000000

    def getAccessToken(self):
        try:
            res = requests.get(
                self.access_token_url,
                auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret),
            )
            print(f"Response: {res}")
        except Exception as err:
            logging.error("Error {}".format(err))
        else:
            token = res.json()["access_token"]
            self.headers = {"Authorization": "Bearer %s" % token}
            return token

    class Decorators:
        @staticmethod
        def refreshToken(decorated):
            def wrapper(gateway, *args, **kwargs):
                if (
                    gateway.access_token_expiration
                    and time.time() > gateway.access_token_expiration
                ):
                    token = gateway.getAccessToken()
                    gateway.access_token = token
                return decorated(gateway, *args, **kwargs)
            return wrapper

    def generate_password(self):
        """Generates mpesa api password using the provided shortcode and passkey"""
        self.timestamp = now.strftime("%Y%m%d%H%M%S")
        password_str = (settings.MPESA_SHORTCODE + settings.MPESA_PASSKEY + self.timestamp)
        password_bytes = password_str.encode("ascii")
        return base64.b64encode(password_bytes).decode("utf-8")

    @Decorators.refreshToken
    def stk_push(
        self, phone_number, amount, callback_url, account_reference, transaction_desc
    ):
        if str(account_reference).strip() == "":
            raise MpesaInvalidParameterException("Account reference cannot be blank")
        if str(transaction_desc).strip() == "":
            raise MpesaInvalidParameterException(
                "Transaction description cannot be blank"
            )
        if not isinstance(amount, int):
            raise MpesaInvalidParameterException("Amount must be an integer")

        phone_number = phone_number
        business_shortcode = self.business_shortcode
        timestamp = self.timestamp
        password = self.password

        req_data = {
            "BusinessShortCode": business_shortcode,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone_number,
            "PartyB": business_shortcode,
            "PhoneNumber": phone_number,
            "CallBackURL": callback_url,
            "AccountReference": account_reference,
            "TransactionDesc": transaction_desc,
        }

        try:
            res = requests.post(
                self.checkout_url, json=req_data, headers=self.headers, timeout=30
            )
            response = mpesa_response(res)

            return response
        except requests.exceptions.ConnectionError:
            raise MpesaConnectionError("Connection failed")
        except Exception as ex:
            raise MpesaConnectionError(str(ex))

    @Decorators.refreshToken
    def c2b(self, amount, phone_number, bill_reference_number):
        if str(bill_reference_number).strip() == "":
            raise MpesaInvalidParameterException("Bill reference cannot be blank")
        if str(phone_number).strip() == "":
            raise MpesaInvalidParameterException(
                "Transaction description cannot be blank"
            )
        if not isinstance(amount, int):
            raise MpesaInvalidParameterException("Amount must be an integer")

        req_data = {
            "CommandID": "CustomerPaybillOnline",
            "Amount": amount,
            "Msisdn": phone_number,
            "BillRefNumber": bill_reference_number,
            "ShortCode": self.business_shortcode,
        }

        try:
            res = requests.post(
                self.checkout_url, json=req_data, headers=self.headers, timeout=30
            )
            response = mpesa_response(res)

            return response
        except requests.exceptions.ConnectionError:
            raise MpesaConnectionError("Connection failed")
        except Exception as ex:
            raise MpesaConnectionError(str(ex))
