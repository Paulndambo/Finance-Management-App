# Generated by Django 5.1.1 on 2024-11-06 08:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("invoices", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoiceitem",
            name="amount",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
    ]
