# Generated by Django 5.1.1 on 2024-10-23 16:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("integrations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chimmoneypaymentrequest",
            name="payment_id",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="chimmoneypaymentrequest",
            name="payment_link",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="chimmoneypaymentrequest",
            name="payment_reference",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
