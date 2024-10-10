from decimal import Decimal
from django.shortcuts import render, redirect
from django.db import transaction
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from rest_framework import generics, status
from rest_framework.response import Response

from finances.models import Expenditure, Income, IncomeRecord
from finances.serializers import ExpenditureSerializer
# Create your views here.
months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
years_list = [2024, 2025, 2026, 2028, 2029, 2030]
income_sources = [
    "Salary", "Freelancing", "Loan Repayments", "Dividends", "Gifts", "Family Support", "Commission",
    "Services", "Investments", "Business Profits", "Other"
]

payment_methods = ["Cash", "Card", "Cheque", "Bank Transfer", "Mpesa", "Other"]
@login_required(login_url="/users/login")
def income(request):
    income = Income.objects.filter(user=request.user).order_by("-created")
    paginator = Paginator(income, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        "page_obj": page_obj,
        "months": months_list,
        "years": years_list,
    }
    return render(request, "income/income.html", context)

@login_required(login_url="/users/login")
def new_income(request):
    if request.method == "POST":
        income = Income.objects.create(
            user = request.user,
            amount = 0,
            month = request.POST.get("month"),
            year = int(request.POST.get("year")),
        )
        return redirect("income")
    return render(request, "income/new_income.html")


@login_required(login_url="/users/login")
def edit_income(request):
    if request.method == "POST":
        income = Income.objects.get(id=request.POST.get("income_id"))
        income.month = request.POST.get("month")
        income.year = int(request.POST.get("year"))
        income.save()
        return redirect("income")
    return render(request, "income/edit_income.html")


@login_required(login_url="/users/login")
def delete_income(request):
    if request.method == "POST":
        income = Income.objects.get(id=request.POST.get("income_id"))
        income.delete()
        return redirect("income")
    return render(request, "income/delete_income.html")


@login_required(login_url="/users/login")
def income_records(request, id):
    income = Income.objects.get(id=id)
    income_records = IncomeRecord.objects.filter(income=income).order_by("-created")
    paginator = Paginator(income_records, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "income": income,
        "income_sources": income_sources,
        "payment_methods": payment_methods
    }
    return render(request, "income/records/income_records.html", context)


@login_required(login_url="/users/login")
def new_income_record(request):
    if request.method == "POST":
        income = Income.objects.get(id=request.POST.get("income_id"))
        record = IncomeRecord.objects.create(
            user = request.user,
            income = income,
            amount = request.POST.get("amount"),
            payment_method = request.POST.get("payment_method"),
            source = request.POST.get("source"),
            received_from = request.POST.get("received_from")
        )
        record.income.amount += Decimal(record.amount)
        record.income.save()
        return redirect(f"/finances/income/{income.id}/records")
    return render(request, "income/records/new_income_record.html")


@login_required(login_url="/users/login")
def edit_income_record(request):
    if request.method == "POST":
        record = IncomeRecord.objects.get(id=request.POST.get("income_record_id"))
        record.payment_method = request.POST.get("payment_method")
        record.source = request.POST.get("source")
        record.received_from = request.POST.get("received_from")
        record.save()
        return redirect(f"/finances/income/{record.income.id}/records")
    return render(request, "income/records/edit_income_record.html")


@login_required(login_url="/users/login")
def delete_income_record(request):
    if request.method == "POST":
        record = IncomeRecord.objects.get(id=request.POST.get("income_record_id"))
        record.income.amount -= Decimal(record.amount)
        record.income.save()
        record.delete()
        return redirect(f"/finances/income/{record.income.id}/records")
    return render(request, "income/records/delete_income_record.html")