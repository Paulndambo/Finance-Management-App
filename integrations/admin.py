from django.contrib import admin

from integrations.models import ChimmoneyPaymentRequest
# Register your models here.
@admin.register(ChimmoneyPaymentRequest)
class ChimmoneyPaymentRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'payment_id', 'paid', 'payment_link', 'payment_reference', 'amount', 'phone_number', 'payer_email')