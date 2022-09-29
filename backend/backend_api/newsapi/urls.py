from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryList, name="category"),
    path('category/<int:pk>', views.CategoryList, name="category"),
    path('newsdata/', views.NewsList, name="newsList"),
    path('newsdata/<int:pk>', views.NewsList, name="newsList"),
]
