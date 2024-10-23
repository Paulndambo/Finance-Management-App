from django.urls import path
from integrations.chimmoney.views import chimmoney_payment_request, payment_requests, delete_payment_request, payment_request_callback


urlpatterns = [
    path("payment-requests/", payment_requests, name="payment-requests"),
    path("payment-request/", chimmoney_payment_request, name="payment-request"),
    path("delete-payment-request/", delete_payment_request, name="delete-payment-request"),
    path("payment-request-callback/", payment_request_callback, name="payment-request-callback"),
]