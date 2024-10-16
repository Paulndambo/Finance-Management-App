from django.urls import path
from invoices.views import invoices, invoice_details, new_invoice, edit_invoice, delete_invoice

urlpatterns = [
    path("", invoices, name="invoices"),
    path("<id>/details/", invoice_details, name="invoice-details"),
    path("new-invoice/", new_invoice, name="new-invoice"),
    path("edit-invoice/", edit_invoice, name="edit-invoice"),
    path("delete-invoice/", delete_invoice, name="delete-invoice"),
]