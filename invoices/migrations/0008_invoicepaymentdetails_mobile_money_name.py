# Generated by Django 5.1.1 on 2024-11-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("invoices", "0007_invoicepaymentdetails_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoicepaymentdetails",
            name="mobile_money_name",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
