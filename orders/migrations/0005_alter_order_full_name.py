# Generated by Django 4.0.3 on 2022-03-24 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_total_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(max_length=250),
        ),
    ]