# Generated by Django 4.1.1 on 2022-11-04 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_orders_zip_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='itemsJson',
        ),
        migrations.AddField(
            model_name='orders',
            name='items_json',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='mobilenumber',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='orders',
            name='zip_code',
            field=models.CharField(default='', max_length=10),
        ),
    ]