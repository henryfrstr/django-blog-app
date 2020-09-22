from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'title_tag',
            'author',
            'description'
        ]
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Your Title'}),
            'title_tag': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Title Tag'}),
            'author': forms.Select(attrs={"class": "form-control", 'placeholder': 'Your Name'}),
            'description': forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Description'}),
        }

        # ordering = ["-id"]

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'title_tag',
            'description'
        ]
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Your Title'}),
            'title_tag': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Title Tag'}),
            'description': forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Description'}),
        }

        
