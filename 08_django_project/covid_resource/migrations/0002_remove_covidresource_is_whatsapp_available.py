# Generated by Django 3.2 on 2021-04-24 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid_resource', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='covidresource',
            name='is_whatsapp_available',
        ),
    ]
