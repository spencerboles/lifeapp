# Generated by Django 4.0.6 on 2022-07-31 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_account_balance_account_description_account_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='is_revenue',
        ),
        migrations.AddField(
            model_name='bucket',
            name='budget_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='bucket',
            name='is_revenue',
            field=models.BooleanField(default=False),
        ),
    ]
