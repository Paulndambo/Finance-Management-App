from django.urls import path
from loans.views import loans, new_loan, loan_details, edit_loan, delete_loan, make_loan_payment, delete_loan_payment, edit_loan_payment

urlpatterns = [
    path("", loans, name="loans"),
    path("<int:id>/details/", loan_details, name="loan-details"),
    path("new-loan/", new_loan, name="new-loan"),
    path("edit-loan/", edit_loan, name="edit-loan"),
    path("delete-loan/", delete_loan, name="delete-loan"),
    path("make-payment/", make_loan_payment, name="make-payment"),
    path("delete-payment/", delete_loan_payment, name="delete-payment"),
    path("edit-payment/", edit_loan_payment, name="edit-payment"),
]