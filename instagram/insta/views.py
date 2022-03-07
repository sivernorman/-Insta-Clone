from email import utils
from django.shortcuts import get_object_or_404, render,redirect
from django.utils import timezone

from .models import Post
from django.views.generic import ListView,CreateView,DetailView

 
# Create your views here.

 

def PostListView(request):
    posts=Post.objects.all()
    context={"posts":posts}  
    return render(request,"insta/post_list.html",context)


def PostCreateView(request):  
    context={}  
    return render(request,"insta/post_create.html",context)


def form_invalid(self,form):
    print(form.cleaned_data)
    form.instance.author = self.request.user
    return super().form_valid(form)


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    def get_object(self):
        id_=self.kwargs.get('id')
        return  get_object_or_404(post,id=id)

# .filter(Created_date_lte=timezone.now())

        # .filter(created_date_lte(timezone.now()).order_by('-created_date') 