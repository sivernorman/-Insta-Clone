from email import utils
from pyexpat import model
from django.shortcuts import get_object_or_404, render,redirect
from django.utils import timezone
from .forms import PostForm
from .models import Post
from django.views.generic import ListView,CreateView,DetailView

 
# Create your views here.

 

class PostListView(ListView):
    model=Post
    template_name='insta/post_list.html'
    def get_context_data(self, *args, **kwargs):
        posts=Post.objects.all()
        context = super(PostListView,self).get_context_data(*args, **kwargs)
        context={"posts":posts}  
        return context 


class PostCreateView(CreateView): 
    model=Post 
    form_class = PostForm
    template_name = 'insta/post_create.html'

def form_invalid(self,form):
    print(form.cleaned_data)
    form.instance.author = self.request.user
    return super().form_valid(form)


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    def get_object(self):
        id_=self.kwargs.get('id')
        return  get_object_or_404(Post,id=id)

# .filter(Created_date_lte=timezone.now())

        # .filter(created_date_lte(timezone.now()).order_by('-created_date') 