from lipia.models import ServiceProvider
from lipia.utils import MpesaGateWay
from decimal import Decimal

def process_multi_merchant_mpesa_payments(phone_number: str, amount: Decimal, pay_type: str, business_number: str, token: str):
    try:
        service_provider = ServiceProvider.objects.get(bill_number=business_number, bill_number_type=pay_type)

        make_payment = MpesaGateWay(
            business_shortcode=business_number,
            consumer_key=service_provider.consumer_key,
            consumer_secret=service_provider.consumer_secret,
            callback_url=service_provider.callback_url,
            phone_number=phone_number,
            amount=int(amount),
            account_reference=f"{service_provider.name} Bill Payments",
            transaction_desc=f"{service_provider.name} Bill Payments",
            token=token
        )

        make_payment.stk_push()
        

        print("********************Payment Initiated Successfully********************")
        print(f"Customer: {phone_number} is paying: {service_provider.name} Kes: {amount} Through: {business_number}")
        print("********************Payment Initiated Successfully********************")
    except Exception as e:
        raise e
