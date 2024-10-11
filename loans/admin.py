from django.contrib import admin

from loans.models import Loan, LoanRepayment


# Register your models here.
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "given_by",
        "amount",
        "amount_paid",
        "amount_to_repay",
        "duration",
        "installment",
    )


@admin.register(LoanRepayment)
class LoanRepaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "loan", "amount", "created")
