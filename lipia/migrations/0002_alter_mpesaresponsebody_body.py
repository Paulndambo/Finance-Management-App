# Generated by Django 4.1.1 on 2023-03-10 23:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lipia", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mpesaresponsebody",
            name="body",
            field=models.JSONField(),
        ),
    ]