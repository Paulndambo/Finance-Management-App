from django.urls import path
from finances.views import (
    income,
    new_income,
    edit_income,
    delete_income,
    income_records,
    new_income_record,
    edit_income_record,
    delete_income_record,
    investments,
    new_investment,
    delete_investment,
    edit_investment,
    expenditures,
    new_expenditure,
    edit_expenditure,
    delete_expenditure,
)

from finances.savings.views import savings, new_saving, edit_saving, delete_saving

urlpatterns = [
    path("income/", income, name="income"),
    path("new-income/", new_income, name="new-income"),
    path("edit-income/", edit_income, name="edit-income"),
    path("delete-income/", delete_income, name="delete-income"),
    path("income/<int:id>/records/", income_records, name="income-records"),
    path("new-income-record/", new_income_record, name="new-income-record"),
    path("edit-income-record/", edit_income_record, name="edit-income-record"),
    path("delete-income-record/", delete_income_record, name="delete-income-record"),
    path("investments/", investments, name="investments"),
    path("new-investment/", new_investment, name="new-investment"),
    path("edit-investment/", edit_investment, name="edit-investment"),
    path("delete-investment/", delete_investment, name="delete-investment"),
    
    path("expenditures/", expenditures, name="expenditures"),
    path("new-expenditure/", new_expenditure, name="new-expenditure"),
    path("edit-expenditure/", edit_expenditure, name="edit-expenditure"),
    path("delete-expenditure/", delete_expenditure, name="delete-expenditure"),
    
    path("savings/", savings, name="savings"),
    path("new-savings/", new_saving, name="new-savings"),
    path("edit-savings/", edit_saving, name="edit-savings"),
    path("delete-savings/", delete_saving, name="delete-savings"),
]
