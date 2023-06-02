# Generated by Django 4.1.7 on 2023-06-02 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lipia', '0006_delete_mpesaauthtoken_serviceprovider_ussd_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceprovider',
            name='callback_url',
            field=models.URLField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='consumer_key',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='consumer_secret',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
