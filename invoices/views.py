from decimal import Decimal
from django.shortcuts import render, redirect
from django.db import transaction
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from invoices.models import Invoice, InvoiceItem

INVOICE_STATUSES = ["Pending", "Paid",  "Cancelled", "Declined", "Defaulted"]
# Create your views here.
@login_required(login_url="/users/login")
def invoices(request):
    invoices = Invoice.objects.filter(user=request.user).order_by("-created")
    
    if request.method == "POST":
        search_text = request.POST.get("search_text")
        invoices = Invoice.objects.filter(user=request.user).filter(
            Q(invoice_number__icontains=search_text) | Q(description__icontains=search_text) | Q(client__icontains=search_text)
        ).order_by("-created")
        
    paginator = Paginator(invoices, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        "page_obj": page_obj,
        "invoice_statuses": INVOICE_STATUSES
    }
    
    return render(request, "invoices/invoices.html", context)


@login_required(login_url="/users/login")
def invoice_details(request, id):
    invoice = Invoice.objects.get(id=id)
    invoice_items = InvoiceItem.objects.filter(invoice=invoice)
    
    context = {
        "invoice": invoice,
        "invoice_items": invoice_items
    }
    
    return render(request, "invoices/invoice_details.html", context)


@login_required(login_url="/users/login")
def new_invoice(request):
    if request.method == "POST":
        due_date = request.POST.get("due_date")
        invoice_date = request.POST.get("invoice_date")
        invoice = Invoice.objects.create(
            user=request.user,
            client_name=request.POST.get("client_name"),
            client_email=request.POST.get("client_email"),
            client_phone=request.POST.get("client_phone"),
            client_address=request.POST.get("client_address"),
            invoice_date=invoice_date,
            due_date=due_date,
        )
        invoice.invoice_number = f"INV-{invoice.id}/{invoice.created.date().year}"
        invoice.save()
        
        print(f"Invoice Due Date: {due_date}, Invoice Date: {invoice_date}")
        
        return redirect(f"/invoices/{invoice.id}/details")
    return render(request, "invoices/new_invoice.html")


@login_required(login_url="/users/login")
def edit_invoice(request):
    if request.method == "POST":
        invoice = Invoice.objects.get(id=request.POST.get("invoice_id"))
        invoice_status = request.POST.get("status")
        
        print(f"Invoice Status: {invoice_status}")
        
        due_date = request.POST.get("due_date")
        invoice_date = request.POST.get("invoice_date")
        invoice.client_name = request.POST.get("client_name")
        invoice.client_email = request.POST.get("client_email")
        invoice.client_phone = request.POST.get("client_phone")
        invoice.client_address = request.POST.get("client_address")
        invoice.status = invoice_status
        invoice.invoice_date = invoice_date if invoice_date else invoice.invoice_date
        invoice.due_date = due_date if due_date else invoice.due_date
        invoice.save()
        return redirect(f"/invoices/{invoice.id}/details")
    return render(request, "invoices/edit_invoice.html")


@login_required(login_url="/users/login")
def delete_invoice(request):
    if request.method == "POST":
        invoice = Invoice.objects.get(id=request.POST.get("invoice_id"))
        invoice.delete()
        return redirect("invoices")
    return render(request, "invoices/delete_invoice.html")