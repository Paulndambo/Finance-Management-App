from django.contrib import admin

from finances.models import Expenditure
# Register your models here.
@admin.register(Expenditure)
class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "budget", "allocation", "amount"]
