# Generated by Django 4.0.3 on 2022-03-31 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_price_alter_product_promotion_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='promotion_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
