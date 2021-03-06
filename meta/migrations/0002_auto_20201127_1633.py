# Generated by Django 3.1.3 on 2020-11-27 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiv0', '0002_auto_20201127_1633'),
        ('meta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttypes',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_types', to='apiv0.product'),
        ),
        migrations.CreateModel(
            name='ProductFibers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.CharField(blank=True, max_length=32, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_fibers', to='apiv0.product')),
            ],
        ),
    ]
