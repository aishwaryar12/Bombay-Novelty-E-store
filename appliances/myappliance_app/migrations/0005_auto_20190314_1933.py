# Generated by Django 2.1.7 on 2019-03-14 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappliance_app', '0004_auto_20190314_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='customer_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='billing',
            name='order_id',
            field=models.CharField(default='', max_length=200),
        ),
    ]