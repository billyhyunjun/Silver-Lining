# Generated by Django 5.0.6 on 2024-05-22 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.PositiveIntegerField(),
        ),
    ]
