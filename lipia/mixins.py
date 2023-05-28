from lipia.utils import generate_payment_timestamps, get_mpesa_transaction_password
import requests
from requests.auth import HTTPBasicAuth
import json

from django.conf import settings

class MpesaPaymentProcessingMixin(object):
    def __init__(self, data):
        self.data = data

    def run(self):
        self.__authenticate_to_mpesa()
        self.__process_mpesa_payment()

    def __authenticate_to_mpesa(self):
        response = requests.get(
            settings.MPESA_AUTH_URL,
            auth=HTTPBasicAuth(settings.MPESA_USERNAME, settings.MPESA_PASSWORD)
        )
        token = json.loads(response.content)['access_token']

        return token

    def __process_mpesa_payment(self):
        phone_number = self.data["phone_number"]
        password = get_mpesa_transaction_password(self.data["merchant_number"], settings.MPESA_PASS_KEY)
        time_stamp = generate_payment_timestamps()
        business_short_code = self.data["merchant_number"]

        user_obj = {
            "phone_number": phone_number,
            "password": password,
            "time_stamp": time_stamp,
            "business_short_code": business_short_code
        }
        print(user_obj)

        data ={
            "BusinessShortCode": 174379,
            "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjMwMzExMDIzNDM5",
            "Timestamp": str(time_stamp),
            "TransactionType": "CustomerBuyGoodsOnline",
            "Amount": 1,
            "PartyA": 254745491093,
            "PartyB": 174379,
            "PhoneNumber": 254745491093,
            "CallBackURL": "https://cd66-105-160-122-64.eu.ngrok.io/lipia/lipa-na-mpesa/",
            "AccountReference": "DaboPay",
            "TransactionDesc": "Payment of X" 
        }
        token = self.__authenticate_to_mpesa()
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

        response = requests.post(settings.MPESA_LIPA_URL, headers=headers, json=data)
        print(json.loads(response.content))


        
