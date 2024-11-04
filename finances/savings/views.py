from decimal import Decimal
from datetime import timedelta, datetime
import calendar

from django.shortcuts import render, redirect
from django.db import transaction
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from rest_framework import generics, status
from rest_framework.response import Response

from finances.models import Saving


date_today = datetime.now().date()
month_name = calendar.month_name[date_today.month]
year = date_today.year

def savings(request):
    savings = Saving.objects.filter(user=request.user).order_by("created")
    
    context = {
        "savings": savings,
    }
    return render(request, "savings/savings.html")


def new_saving(request):
    if request.method == "POST":
        month = request.POST.get("month")
        saving = Saving.objects.create(
            user=request.user,
            amount=request.POST.get("amount"),
            month=month if month else month_name,
            year=year,
            saved_on=request.POST.get("saved_on"),
        )
        return redirect("savings")
    return render(request, "savings/new_saving.html")


def edit_saving(request):
    if request.method == "POST":
        saving = Saving.objects.get(id=request.POST.get("saving_id"))
        saving.amount = request.POST.get("amount")
        saving.month = request.POST.get("month")
        saving.year = request.POST.get("year")
        saving.saved_on = request.POST.get("saved_on")
        saving.save()
        return redirect("savings")
    return render(request, "savings/edit_saving.html")


def delete_saving(request):
    if request.method == "POST":
        saving = Saving.objects.get(id=request.POST.get("saving_id"))
        saving.delete()
        return redirect("savings")
    return render(request, "savings/delete_saving.html")