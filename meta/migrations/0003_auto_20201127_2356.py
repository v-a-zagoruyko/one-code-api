# Generated by Django 3.1.3 on 2020-11-27 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0002_auto_20201127_1633'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productfibers',
            options={'verbose_name': 'Состав и описание', 'verbose_name_plural': 'Состав и описание'},
        ),
        migrations.AlterModelOptions(
            name='producttypes',
            options={'verbose_name': 'Размер', 'verbose_name_plural': 'Размеры'},
        ),
    ]
