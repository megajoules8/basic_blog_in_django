from django.urls import path
from . import views #this grabs the views from the blog application

# You have to add this file to make a view available at a URL.
# note this file wasn't here in the initial setup, you have to create it.

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #this is the URL pattern for the post_detail view, which we will create in views.py
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]