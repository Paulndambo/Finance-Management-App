# Generated by Django 5.1.1 on 2024-11-04 00:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finances", "0009_expenditure_description"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Saving",
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
                ("saved_on", models.CharField(max_length=255, null=True)),
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