from django.urls import path
from finances.views import income, new_income, edit_income, delete_income, income_records, new_income_record, edit_income_record, delete_income_record

urlpatterns = [
    path("income/", income, name="income"),
    path("new-income/", new_income, name="new-income"),
    path("edit-income/", edit_income, name="edit-income"),
    path("delete-income/", delete_income, name="delete-income"),
    path("income/<int:id>/records/", income_records, name="income-records"),
    path("new-income-record/", new_income_record, name="new-income-record"),
    path("edit-income-record/", edit_income_record, name="edit-income-record"),
    path("delete-income-record/", delete_income_record, name="delete-income-record"),
]