# Generated by Django 5.1.1 on 2024-10-12 16:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("budgets", "0009_alter_budgetallocation_allocation_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="budgetallocation",
            name="category",
        ),
    ]
