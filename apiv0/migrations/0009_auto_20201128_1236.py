# Generated by Django 3.1.3 on 2020-11-28 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiv0', '0008_auto_20201128_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='add_to_main_page',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='collection',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='collection',
            name='is_visible',
            field=models.BooleanField(default=False),
        ),
    ]