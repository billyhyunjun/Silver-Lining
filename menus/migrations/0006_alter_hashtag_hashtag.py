# Generated by Django 5.0.6 on 2024-05-22 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0005_remove_hashtag_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='hashtag',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
