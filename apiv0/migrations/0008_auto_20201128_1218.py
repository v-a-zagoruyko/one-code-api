# Generated by Django 3.1.3 on 2020-11-28 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0003_auto_20201127_2356'),
        ('apiv0', '0007_auto_20201128_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='products',
        ),
        migrations.AddField(
            model_name='sale',
            name='time_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='time_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='saleproducts',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_size', to='meta.sizes'),
        ),
    ]
