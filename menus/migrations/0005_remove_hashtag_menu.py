# Generated by Django 5.0.6 on 2024-05-21 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0004_alter_hashtag_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashtag',
            name='menu',
        ),
    ]