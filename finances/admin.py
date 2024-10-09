from django.contrib import admin

from finances.models import Expenditure, Income, IncomeRecord
# Register your models here.
@admin.register(Expenditure)
class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "budget", "allocation", "amount"]


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "year", "month", "amount"]
    

@admin.register(IncomeRecord)
class IncomeRecordAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "income__month", "income__year", "amount"]