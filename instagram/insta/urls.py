from django.conf import settings
from django.urls import path,include
from insta.views import PostListView,PostCreateView,PostDetailView
 
app_name = 'insta'
urlpatterns = [
    path('',PostListView,name='post_list'),
    path('new/', PostCreateView,name='post_create'),
    path('new/',PostDetailView.as_view,name='post_detail'),


 ]


 