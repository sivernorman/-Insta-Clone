from django.conf import settings
from django.urls import path,include
from insta.views import PostListView

app_name = 'insta'
urlpatterns = [
    path('',PostListView,name='post_list'),
]


 