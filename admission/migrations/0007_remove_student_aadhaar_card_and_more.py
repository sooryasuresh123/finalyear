# Generated by Django 4.2.11 on 2025-02-21 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0006_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='aadhaar_card',
        ),
        migrations.RemoveField(
            model_name='student',
            name='income_certificate',
        ),
        migrations.RemoveField(
            model_name='student',
            name='ncc_nss_certificate',
        ),
        migrations.RemoveField(
            model_name='student',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='student',
            name='plus_two_certificate',
        ),
        migrations.RemoveField(
            model_name='student',
            name='sslc_certificate',
        ),
    ]
