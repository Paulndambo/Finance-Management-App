# Generated by Django 5.1.1 on 2024-10-10 11:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("loans", "0003_loan_given_by_loan_loan_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="loan",
            name="fully_paid",
            field=models.BooleanField(default=False),
        ),
    ]