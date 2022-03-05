from multiprocessing import context
from re import template
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
 
# Create your views here.

class PostListView():
    template_name = "insta/post_list"
    queryset = Post.objects.all()
    context_object_name ='posts'