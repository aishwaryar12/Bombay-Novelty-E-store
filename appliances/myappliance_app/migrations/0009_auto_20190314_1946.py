# Generated by Django 2.1.7 on 2019-03-14 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myappliance_app', '0008_auto_20190314_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billing',
            name='gst',
        ),
        migrations.RemoveField(
            model_name='billing',
            name='shipping_charges',
        ),
        migrations.RemoveField(
            model_name='billing',
            name='total',
        ),
        migrations.RemoveField(
            model_name='billing',
            name='total_tax',
        ),
    ]
