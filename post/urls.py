from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('blogs/',blogs,name='blogs'),
    path('blog/<str:slug>/', blog_details, name='blog_details'),
    path('search_blogs/', search_blogs, name='search_blogs'),
]