from django.contrib import admin
from django.urls import path

from . import views
app_name = 'posts'
urlpatterns=[
    path('new/',views.post, name= 'post_new'),
]