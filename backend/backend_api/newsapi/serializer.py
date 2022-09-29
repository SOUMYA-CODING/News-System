from rest_framework import serializers
from . models import Category, NewsData


# Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


# NewsData
class NewsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsData
        fields = "__all__"
