from multiprocessing import context
from re import template
from django.shortcuts import render

from insta.forms import postForm
from .models import Post
from django.views.generic import ListView,CreateView
 
# Create your views here.

 

def PostListView(request):
    posts=Post.objects.all()  
    context={"posts":posts}  
    return render(request,"insta/post_list.html",context)


def PostCreateView(request):  
    context={}  
    return render(request,"insta/post_create.html",context)