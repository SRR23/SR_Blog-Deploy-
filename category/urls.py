from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('category_blogs/<str:slug>/', category_blogs, name='category_blogs'),
]