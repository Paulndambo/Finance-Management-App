# Generated by Django 5.1.1 on 2024-10-12 15:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("budgets", "0006_alter_budgetallocation_allocation_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="budget",
            name="income",
        ),
        migrations.RemoveField(
            model_name="budget",
            name="name",
        ),
    ]
