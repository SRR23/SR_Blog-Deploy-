
from django.urls import path
from .views import *
urlpatterns = [
    path('add_reply/<int:blog_id>/<int:comment_id>/', add_reply, name='add_reply'),
    path('my_blogs/', my_blogs, name='my_blogs'),
    path('add_blog/', add_blog, name='add_blog'),
    path('update_blog/<str:slug>/', update_blog, name='update_blog'),
    path('favourite_blog/<int:id>/', favourite_blog, name='favourite_blog'),
    path('favourite/', favourites_list, name='favourite'),
    
    path('login/',login_user,name='login'),
    path('profile/', profile, name='profile'),
    path('change_profile_picture/', change_profile_picture, name='change_profile_picture'),
    path('view_user_information/<str:username>/', view_user_information, name="view_user_information"),
    path('logout/', logout_user, name='logout'),
    path('register_user/', register_user, name='register_user'),
]