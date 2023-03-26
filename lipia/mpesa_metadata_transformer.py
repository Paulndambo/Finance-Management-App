from datetime import datetime

def mpesa_callback_item_dismantler(item: list):
    receipt_number = [x["Value"] for x in item if x['Name'] == "MpesaReceiptNumber"][0]
    phone_number = [x["Value"] for x in item if x['Name'] == "PhoneNumber"][0]
    transaction_timestamp = [x["Value"] for x in item if x['Name'] == "TransactionDate"][0]
    amount = [x["Value"] for x in item if x['Name'] == "Amount"][0]

    return receipt_number, phone_number, transaction_timestamp, amount


def mpesa_metadata_transformative_function(stkCallback):
    transformed_mpesa_metadata_object = {
        "merchant_request_id": stkCallback["MerchantRequestID"],
        "checkout_request_id": stkCallback["CheckoutRequestID"],
        "transaction_result_code": stkCallback["ResultCode"],
        "receipt_number": [x["Value"] for x in stkCallback["CallbackMetadata"]["Item"] if x['Name'] == "MpesaReceiptNumber"][0],
        "phone_number": [x["Value"] for x in stkCallback["CallbackMetadata"]["Item"] if x['Name'] == "PhoneNumber"][0],
        "transaction_timestamp": [x["Value"]for x in stkCallback["CallbackMetadata"]["Item"] if x['Name'] == "TransactionDate"][0],
        # transaction_date = datetime.fromtimestamp(transaction_timestamp)
        "amount": [x["Value"] for x in stkCallback["CallbackMetadata"]["Item"] if x['Name'] == "Amount"][0]
    }

    return transformed_mpesa_metadata_object