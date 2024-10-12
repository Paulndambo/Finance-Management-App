# Generated by Django 5.1.1 on 2024-10-12 15:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("budgets", "0007_remove_budget_income_remove_budget_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="budget",
            name="amount_budgeted",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
    ]