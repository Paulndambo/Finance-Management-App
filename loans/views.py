from decimal import Decimal
from django.shortcuts import render, redirect
from django.db import transaction
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from loans.models import Loan, LoanRepayment

# Create your views here.
payment_methods = ["Cash", "Card", "Cheque", "Bank Transfer", "Mpesa", "Other"]
loan_types = ["Received", "Given Out"]

@login_required(login_url="/users/login")
def loans(request):
    user = request.user
    loans = Loan.objects.filter(user=user).order_by("-created")

    paginator = Paginator(loans, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    total_borrowed = sum(
        list(
            Loan.objects.filter(user=user)
            .filter(loan_type="Received")
            .values_list("amount_to_repay", flat=True)
        )
    )
    total_given = sum(
        list(
            Loan.objects.filter(user=user)
            .filter(loan_type="Given Out")
            .values_list("amount_to_repay", flat=True)
        )
    )
    total_repaid = sum(
        list(
            Loan.objects.filter(user=user)
            .filter(user=user)
            .values_list("amount_paid", flat=True)
        )
    )

    borrowed_loans_repaid = sum(
        list(
            Loan.objects.filter(user=user)
            .filter(loan_type="Received")
            .values_list("amount_paid", flat=True)
        )
    )
    given_loans_repaid = sum(
        list(
            Loan.objects.filter(user=user)
            .filter(loan_type="Given Out")
            .values_list("amount_paid", flat=True)
        )
    )

    context = {
        "page_obj": page_obj,
        "total_borrowed": total_borrowed if total_borrowed else 0,
        "total_given": total_given if total_given else 0,
        "total_repaid": total_repaid if total_repaid else 0,
        "amount_owing": total_borrowed - borrowed_loans_repaid,
        "amount_owed": total_given - given_loans_repaid,
        "loan_types": loan_types,
    }
    return render(request, "loans/loans.html", context)


@login_required(login_url="/users/login")
@transaction.atomic
def new_loan(request):
    if request.method == "POST":
        amount_to_repay = Decimal(request.POST.get("amount_to_repay"))
        installment = int(request.POST.get("installment"))

        loan = Loan.objects.create(
            amount_to_repay=amount_to_repay,
            installment=Decimal(installment),
            given_by=request.POST.get("given_by"),
            user=request.user,
            loan_type=request.POST.get("loan_type"),
            duration=request.POST.get("duration"),
            date_due=request.POST.get("date_due"),
            amount=request.POST.get("amount"),
        )

        return redirect("loans")

    return render(request, "loans/new_loan.html")


@login_required(login_url="/users/login")
def loan_details(request, id):
    user = request.user
    loan = Loan.objects.get(id=id)

    payments = LoanRepayment.objects.filter(user=user, loan=loan).order_by("-created")

    paginator = Paginator(payments, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, "loan": loan, "payment_methods": payment_methods}
    return render(request, "loans/loan_details.html", context)


@login_required(login_url="/users/login")
def edit_loan(request):
    if request.method == "POST":
        loan = Loan.objects.get(id=request.POST.get("loan_id"))

        amount_to_repay = request.POST.get("amount_to_repay")
        installment = request.POST.get("installment")
        given_by = request.POST.get("given_by")
        loan_type = request.POST.get("loan_type")
        duration = request.POST.get("duration")
        date_due = request.POST.get("date_due")
        amount = request.POST.get("amount")

        loan.amount_to_repay = (
            Decimal(amount_to_repay) if amount_to_repay else loan.amount_to_repay
        )
        loan.installment = Decimal(installment) if installment else loan.installment
        loan.given_by = given_by if given_by else loan.given_by
        loan.loan_type = loan_type if loan_type else loan.loan_type
        loan.duration = duration if duration else loan.duration
        loan.date_due = date_due if date_due else loan.date_due
        loan.amount = amount if amount else loan.amount

        loan.save()
        return redirect(f"/loans/{loan.id}/details")
    return render(request, "loans/edit_loan.html")


@login_required(login_url="/users/login")
def delete_loan(request):
    if request.method == "POST":
        loan = Loan.objects.get(id=request.POST.get("loan_id"))
        loan.delete()
        return redirect("loans")
    return render(request, "loans/delete_loan.html")


@login_required(login_url="/users/login")
@transaction.atomic
def make_loan_payment(request):
    if request.method == "POST":
        loan_id = request.POST.get("loan_id")
        amount_paid = Decimal(request.POST.get("amount_paid"))

        loan = Loan.objects.get(id=loan_id)
        loan.amount_paid += amount_paid
        loan.save()

        LoanRepayment.objects.create(
            amount=amount_paid,
            loan=loan,
            user=request.user,
            payment_method=request.POST.get("payment_method"),
        )

        return redirect(f"/loans/{loan_id}/details")
    return redirect("loans")


@login_required(login_url="/users/login")
@transaction.atomic
def edit_loan_payment(request):
    if request.method == "POST":
        payment = LoanRepayment.objects.get(id=request.POST.get("payment_id"))

        initial_amount = payment.amount
        payment.loan.amount_paid -= initial_amount
        payment.loan.save()

        payment.amount = Decimal(request.POST.get("amount"))
        payment.payment_method = request.POST.get("payment_method")
        payment.save()

        payment.loan.amount_paid += payment.amount
        payment.loan.save()
        return redirect(f"/loans/{payment.loan.id}/details")
    return render(request, "loans/edit_loan_payment.html")


@login_required(login_url="/users/login")
def delete_loan_payment(request):
    if request.method == "POST":
        payment = LoanRepayment.objects.get(id=request.POST.get("payment_id"))
        payment.loan.amount_paid -= payment.amount
        payment.loan.save()
        payment.delete()
        return redirect(f"/loans/{payment.loan.id}/details")
    return render(request, "loans/delete_loan_payment.html")
