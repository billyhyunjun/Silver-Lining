# Generated by Django 4.2 on 2024-05-30 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0003_hashtag_hashtag_ja_hashtag_hashtag_zh_cn_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashtag',
            old_name='hashtag_zh_CN',
            new_name='hashtag_zh_hans',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='food_name_zh_CN',
            new_name='food_name_zh_hans',
        ),
    ]
