from django.urls import path
from loans.views import loans, new_loan, loan_details

urlpatterns = [
    path("", loans, name="loans"),
    path("<int:id>/details/", loan_details, name="loan-details"),
    path("new-loan/", new_loan, name="new-loan"),
]