from pyexpat import model
from django import forms
from .models import Post
  

class postForm(forms.ModelForm):
 
    class Meta:
        model=Post
        fields=[
            'image',
            'Caption',
        ]