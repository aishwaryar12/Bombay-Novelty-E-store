# Generated by Django 2.1.7 on 2019-03-14 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myappliance_app', '0005_auto_20190314_1933'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='billing',
            new_name='pbilling',
        ),
    ]