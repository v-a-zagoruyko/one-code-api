# Generated by Django 3.1.3 on 2020-11-29 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0003_auto_20201127_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttypes',
            name='price',
        ),
    ]
