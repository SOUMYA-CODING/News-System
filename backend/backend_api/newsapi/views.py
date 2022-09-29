from rest_framework.decorators import api_view
from rest_framework.response import Response

from . models import Category, NewsData
from . serializer import CategorySerializer, NewsDataSerializer


# Category API
@api_view(['GET'])
def CategoryList(request, pk=None):
    # Get the ID
    id = pk
    # GET
    if request.method == "GET":
        if id is not None:
            category_data = Category.objects.get(id=id)
            serializer = CategorySerializer(category_data)
            return Response(serializer.data)

        list = Category.objects.all()
        serializer = CategorySerializer(list, many=True)
        return Response(serializer.data)


# Category API
@api_view(['GET'])
def NewsList(request, pk=None):
    # Get the ID
    id = pk
    # GET
    if request.method == "GET":
        if id is not None:
            news_data = NewsData.objects.get(id=id)
            serializer = NewsDataSerializer(news_data)
            return Response(serializer.data)

        list = NewsData.objects.all()
        serializer = NewsDataSerializer(list, many=True)
        return Response(serializer.data)
