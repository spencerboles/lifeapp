# Generated by Django 4.0.6 on 2022-08-06 03:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_alter_account_description_alter_bucket_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date_incurred',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
