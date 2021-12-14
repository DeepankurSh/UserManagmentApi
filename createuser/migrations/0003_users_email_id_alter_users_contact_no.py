# Generated by Django 4.0 on 2021-12-13 09:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createuser', '0002_alter_users_contact_no_alter_users_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='email_Id',
            field=models.CharField(blank=True, max_length=320, null=True, unique=True, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$')]),
        ),
        migrations.AlterField(
            model_name='users',
            name='contact_no',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(regex='^[6-9]\\d{9}$')]),
        ),
    ]
