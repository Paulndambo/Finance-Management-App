from django.contrib import admin
from invoices.models import Invoice
# Register your models here.
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ["id", "client_name", "invoice_number", "due_date", "invoice_date", "invoice_amount", "status"]