# Generated by Django 4.1.3 on 2022-11-11 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsfeed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('subtitle', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('image_for_web', models.ImageField(null=True, upload_to='image_for_web')),
                ('image_for_app', models.ImageField(null=True, upload_to='image_for_app')),
                ('is_news_in_picture', models.BooleanField()),
                ('image_for_news_in_picture', models.ImageField(null=True, upload_to='image_for_news_in_picture')),
                ('is_there_any_video', models.BooleanField(default=True)),
                ('video', models.FileField(null=True, upload_to='video')),
                ('video_duratio', models.FloatField()),
                ('visiblity', models.BooleanField()),
                ('is_top_breaking_news', models.BooleanField()),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('send_notification_to_phone', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsfeed.topicscategory')),
            ],
        ),
    ]