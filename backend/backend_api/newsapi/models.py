from django.db import models


# Category
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# NewsData
class NewsData(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="images/", blank=True)
    video = models.ImageField(upload_to="videos/", blank=True)

    def __str__(self):
        return self.name
