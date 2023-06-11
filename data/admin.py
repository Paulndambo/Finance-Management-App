from django.contrib import admin
from data.models import Budget, Bill, Todo, Event
# Register your models here.
@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ["user", "month", "year", "allocated", "expenditure", "amount_saved"]


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ["user", "budget", "name", "bill_type", "allocated", "expenditure", "amount_saved"]

admin.site.register(Todo)
admin.site.register(Event)