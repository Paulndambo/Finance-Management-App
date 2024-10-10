from decimal import Decimal
from django.shortcuts import render, redirect
from django.db import transaction
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from loans.models import Loan, LoanInstallment, LoanRepayment
# Create your views here.
@login_required(login_url="/users/login")
def loans(request):
    user = request.user
    loans = Loan.objects.filter(user=user).order_by("-created")
    
    paginator = Paginator(loans, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    total_borrowed = sum(list(Loan.objects.filter(user=user).filter(loan_type="Received").values_list("amount_to_repay", flat=True)))
    total_given = sum(list(Loan.objects.filter(user=user).filter(loan_type="Given Out").values_list("amount_to_repay", flat=True)))
    total_repaid = sum(list(Loan.objects.filter(user=user).filter(user=user).values_list("amount_paid", flat=True)))
    
    borrowed_loans_repaid = sum(list(Loan.objects.filter(user=user).filter(loan_type="Received").values_list("amount_paid", flat=True)))
    given_loans_repaid = sum(list(Loan.objects.filter(user=user).filter(loan_type="Given Out").values_list("amount_paid", flat=True)))
    
    
    context = {
        "page_obj": page_obj,
        "total_borrowed": total_borrowed if total_borrowed else 0,
        "total_given": total_given if total_given else 0,
        "total_repaid": total_repaid if total_repaid else 0,
        "amount_owing": total_borrowed - borrowed_loans_repaid,
        "amount_owed": total_given - given_loans_repaid
    }
    return render(request, "loans/loans.html", context)


@login_required(login_url="/users/login")
@transaction.atomic
def new_loan(request):
    if request.method == "POST":
        amount_to_repay = Decimal(request.POST.get("amount_to_repay"))
        installments = int(request.POST.get("number_of_installments"))

        loan = Loan.objects.create(
            amount_to_repay=amount_to_repay,
            number_of_installments=installments,
            given_by=request.POST.get("given_by"),
            user=request.user,
            loan_type=request.POST.get("loan_type"),
            duration=request.POST.get("duration"),
            date_due=request.POST.get("date_due"),
            amount=request.POST.get("amount"),
        )
        
        installment_amount = amount_to_repay / installments
        for i, _ in enumerate(range(installments)):
            LoanInstallment.objects.create(
                user=request.user,
                loan=loan,
                amount=installment_amount,
                paid=False
            )
        
        return redirect("loans")
        
    return render(request, "loans/new_loan.html")


@login_required(login_url="/users/login")
def loan_details(request, id):
    user=request.user
    loan = Loan.objects.get(id=id)
    
    installments = LoanInstallment.objects.filter(user=user, loan=loan).order_by("-created")
    payments = LoanRepayment.objects.filter(user=user, loan=loan).order_by("-created")
    
    context = {
        "loan": loan,
        "installments": installments,
        "payments": payments
    }
    return render(request, "loans/loan_details.html", context)