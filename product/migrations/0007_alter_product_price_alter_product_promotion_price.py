# Generated by Django 4.0.3 on 2022-03-31 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_moreimagesvariation_moreimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='promotion_price',
            field=models.FloatField(blank=True),
        ),
    ]
