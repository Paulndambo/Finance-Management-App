from django.urls import path
from finances.views import income, new_income, income_records, new_income_record

urlpatterns = [
    path("income/", income, name="income"),
    path("new-income/", new_income, name="new-income"),
    path("income/<int:id>/records/", income_records, name="income-records"),
    path("new-income-record/", new_income_record, name="new-income-record"),
]