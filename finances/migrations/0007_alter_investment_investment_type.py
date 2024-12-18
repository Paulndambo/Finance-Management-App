# Generated by Django 5.1.1 on 2024-10-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finances", "0006_investment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="investment",
            name="investment_type",
            field=models.CharField(
                choices=[
                    ("Money Market", "Money Market"),
                    ("Stocks", "Stocks"),
                    ("Real Estate", "Real Estate"),
                    ("Business", "Business"),
                    ("Savings", "Savings"),
                    ("Livestock", "Livestock"),
                    ("Farming", "Farming"),
                    ("Other", "Other"),
                ],
                max_length=255,
            ),
        ),
    ]
