from django.contrib import admin
from invoices.models import Invoice, InvoiceItem, InvoicePaymentDetails
# Register your models here.
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ["id", "client_name", "invoice_number", "due_date", "invoice_date", "invoice_amount", "status"]
    
    
@admin.register(InvoicePaymentDetails)
class InvoicePaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ["id","user", "invoice", "payment_method", "mobile_money_provider", "mobile_money_code", "mobile_money_number", "mobile_money_name", "payer_name", "payer_email", "payer_phone_number"]