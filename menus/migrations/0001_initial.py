# Generated by Django 4.2 on 2024-06-10 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.CharField(max_length=255)),
                ('hashtag_ko', models.CharField(max_length=255, null=True)),
                ('hashtag_en', models.CharField(max_length=255, null=True)),
                ('hashtag_ja', models.CharField(max_length=255, null=True)),
                ('hashtag_zh_hans', models.CharField(max_length=255, null=True)),
                ('hashtag_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_hashtag', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100)),
                ('food_name_ko', models.CharField(max_length=100, null=True)),
                ('food_name_en', models.CharField(max_length=100, null=True)),
                ('food_name_ja', models.CharField(max_length=100, null=True)),
                ('food_name_zh_hans', models.CharField(max_length=100, null=True)),
                ('price', models.PositiveIntegerField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='menu_images/')),
                ('hashtags', models.ManyToManyField(related_name='menu_items', to='menus.hashtag')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='hashtag',
            constraint=models.UniqueConstraint(fields=('hashtag', 'hashtag_author'), name='unique_user_hashtag'),
        ),
    ]
