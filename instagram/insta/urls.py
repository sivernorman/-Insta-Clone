from django.conf import settings
from django.urls import path,include
from .views import PostListView,PostCreateView,PostDetailView
 
urlpatterns = [
    path('',PostListView.as_view(),name='post_list'),
    path('post_create/',PostCreateView.as_view(),name='post_create'),
    path('new/',PostDetailView.as_view(),name='post_detail'),


 ]


 