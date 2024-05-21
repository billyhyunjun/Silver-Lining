# Generated by Django 4.2 on 2024-05-21 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0003_hashtag_hashtag_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_hashtags', to='menus.menu'),
        ),
    ]