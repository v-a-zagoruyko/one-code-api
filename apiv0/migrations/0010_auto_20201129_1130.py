# Generated by Django 3.1.3 on 2020-11-29 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiv0', '0009_auto_20201128_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleproducts',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]