# Generated by Django 4.0.3 on 2022-04-03 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_userbase_address_line_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='address_line_1',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='first_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='town_city',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='user_name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
