# Generated by Django 5.1.4 on 2024-12-21 08:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_houseamenities'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='payment_method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.paymentmethod'),
        ),
    ]
