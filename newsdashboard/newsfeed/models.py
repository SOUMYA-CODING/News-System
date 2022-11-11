from django.db import models
from django.contrib.auth.models import User


# Topics Category
class TopicsCategory(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="topic_category_logo/")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# News Feed
class NewsFeed(models.Model):
    category = models.ForeignKey(TopicsCategory, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=250, null=False)
    subtitle = models.CharField(max_length=250, null=False)
    description = models.TextField(null=False)
    image_for_web = models.ImageField(upload_to="image_for_web", null=True)
    image_for_app = models.ImageField(upload_to="image_for_app", null=True)

    is_news_in_picture = models.BooleanField()
    image_for_news_in_picture = models.ImageField(upload_to="image_for_news_in_picture", null=True)

    # If there is video
    is_there_any_video = models.BooleanField(default=True)
    video = models.FileField(upload_to="video", null=True)
    video_duratio = models.FloatField()

    visiblity = models.BooleanField()
    is_top_breaking_news = models.BooleanField()

    uploaded_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    send_notification_to_phone = models.BooleanField()
    # new_link

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

# Comment