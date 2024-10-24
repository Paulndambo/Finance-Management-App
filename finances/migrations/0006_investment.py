# Generated by Django 5.1.1 on 2024-10-11 19:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finances", "0005_incomerecord_received_from"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Investment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "month",
                    models.CharField(
                        choices=[
                            ("January", "January"),
                            ("February", "February"),
                            ("March", "March"),
                            ("April", "April"),
                            ("May", "May"),
                            ("June", "June"),
                            ("July", "July"),
                            ("August", "August"),
                            ("September", "September"),
                            ("October", "October"),
                            ("November", "November"),
                            ("December", "December"),
                        ],
                        max_length=255,
                    ),
                ),
                ("year", models.IntegerField()),
                (
                    "amount",
                    models.DecimalField(decimal_places=2, default=0, max_digits=100),
                ),
                (
                    "investment_type",
                    models.CharField(
                        choices=[
                            ("Money Market", "Money Market"),
                            ("Stocks", "Stocks"),
                            ("Real Estate", "Real Estate"),
                            ("Business", "Business"),
                            ("Savings", "Savings"),
                            ("Other", "Other"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
