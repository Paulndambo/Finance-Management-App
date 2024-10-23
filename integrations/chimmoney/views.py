import requests
from decimal import Decimal
from django.shortcuts import render, redirect
from django.db import transaction
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.conf import settings

from integrations.models import ChimmoneyPaymentRequest

    
@login_required(login_url="/users/login")
def payment_requests(request):
    payment_requests = ChimmoneyPaymentRequest.objects.filter(user=request.user)
    
    paginator = Paginator(payment_requests, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }
    
    return render(request, "integrations/chimmoney/payment_requests.html", context)    
    
@login_required(login_url="/users/login")
def chimmoney_payment_request(request):
    if request.method == "POST":
        with transaction.atomic():
            
            payload = {
                "valueInUSD": request.POST.get("amount"),
                "payerEmail": request.POST.get("payer_email"),
                "amount": request.POST.get("amount"),
                "redirect_url": settings.CHIMMONEY_PAYMENT_REQUEST_CALLBACK,
            }
            
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "X-API-KEY": settings.CHIMMONEY_API_KEY
            }
            
            url = f"{settings.CHIMMONEY_BASE_URL}/payment/initiate"
            response = requests.post(url, json=payload, headers=headers)

            if response.status_code in [200, 201]:
                data = response.json()["data"]
                
                paymentLink = data["paymentLink"]
                paymentRef = data["paymentRef"]
                paymentId = data["t_id"]
                
                pay_object = {
                    "paymentRef": paymentRef,
                    "paymentId": paymentId,
                    "paymentLink": paymentLink
                }
                print(pay_object)
                
                payment_request = ChimmoneyPaymentRequest.objects.create(
                    payer_name=request.POST.get("payer_name"),
                    user=request.user,
                    amount=request.POST.get("amount"),
                    phone_number=request.POST.get("phone_number"),
                    payer_email=request.POST.get("payer_email"),
                    description=request.POST.get("description"),
                    payment_reference=paymentRef,
                    payment_id=paymentId,
                    payment_link=paymentLink,
                )

            else:
                print(response.json())
            return redirect("payment-requests")
    
    return render(request, "integrations/chimmoney/payment_request.html")


def delete_payment_request(request):
    if request.method == "POST":
        id = request.POST.get("payment_id")
        payment_request = ChimmoneyPaymentRequest.objects.get(id=id)
        payment_request.delete()
        return redirect("payment-requests")
    return render(request, "integrations/chimmoney/delete_payment_request.html")


def payment_request_callback(request):
    status = request.GET.get('status')
    tx_ref = request.GET.get('tx_ref')
    transaction_id = request.GET.get('transaction_id')
    
    if status == "successful":
        ref_split = tx_ref.split("_")[:-1]
        ref_split_str = "_".join(ref_split)
        payment_requests = ChimmoneyPaymentRequest.objects.filter(payment_reference=ref_split_str)
        payment_requests.update(paid=True)
        
        return redirect("payment-requests")
        
    
    return render(request, "integrations/chimmoney/payment_request_callback.html")