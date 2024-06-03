from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('tag_blogs/<str:slug>/', tag_blogs, name='tag_blogs'),
]