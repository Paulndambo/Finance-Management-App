from django.contrib import admin
from core.models import BudgetCategory
# Register your models here.
@admin.register(BudgetCategory)
class BudgetCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "active"]