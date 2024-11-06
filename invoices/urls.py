from django.urls import path
from invoices.views import invoices, invoice_details, new_invoice, edit_invoice, delete_invoice, new_invoice_item, delete_invoice_item, edit_invoice_item, add_payment_details

urlpatterns = [
    path("", invoices, name="invoices"),
    path("<id>/details/", invoice_details, name="invoice-details"),
    path("new-invoice/", new_invoice, name="new-invoice"),
    path("edit-invoice/", edit_invoice, name="edit-invoice"),
    path("delete-invoice/", delete_invoice, name="delete-invoice"),

    path("new-invoice-item/", new_invoice_item, name="new-invoice-item"),
    path("delete-invoice-item/", delete_invoice_item, name="delete-invoice-item"),
    path("edit-invoice-item/", edit_invoice_item, name="edit-invoice-item"),
    path("add-payment-details/", add_payment_details, name="add-payment-details"),
]