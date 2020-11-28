# Generated by Django 3.1.3 on 2020-11-28 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiv0', '0006_auto_20201128_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('products', models.ManyToManyField(to='apiv0.Product')),
            ],
            options={
                'verbose_name': 'Распродажа',
                'verbose_name_plural': 'Распродажи',
            },
        ),
        migrations.RenameModel(
            old_name='ProductCollection',
            new_name='Collection',
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'verbose_name': 'Коллекция', 'verbose_name_plural': 'Коллекции'},
        ),
        migrations.CreateModel(
            name='SaleProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveSmallIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_product', to='apiv0.product')),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_products', to='apiv0.sale')),
                ('size', models.ForeignKey(limit_choices_to={'product': models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_product', to='apiv0.product')}, on_delete=django.db.models.deletion.CASCADE, related_name='sale_size', to='apiv0.sale')),
            ],
        ),
    ]