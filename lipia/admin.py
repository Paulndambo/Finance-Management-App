from django.contrib import admin

from lipia.models import MpesaResponseBody, MpesaTransaction

# Register your models here.
@admin.register(MpesaResponseBody)
class MpesaResponseBodyAdmin(admin.ModelAdmin):
    list_display = ["id", "body", "created"]
    
    

@admin.register(MpesaTransaction)
class MpesaTransactionAdmin(admin.ModelAdmin):
    list_display = ["id", "receipt_number", "phone_number", "amount"]
