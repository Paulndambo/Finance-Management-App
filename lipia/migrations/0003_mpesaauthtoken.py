# Generated by Django 4.1.7 on 2023-03-12 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lipia', '0002_alter_mpesaresponsebody_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='MpesaAuthToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]