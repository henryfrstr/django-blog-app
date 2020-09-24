from django import forms
from .models import Post, Category

choises = Category.objects.all().values_list('name', 'name')

choise_list = []
for item in choises:
    choise_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'title_tag',
            'author',
            'category',
            'description'
        ]
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Your Title'}),
            'title_tag': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Title Tag'}),
            'author': forms.Select(attrs={"class": "form-control", 'placeholder': 'Your Name'}),
            'category': forms.Select(choices=choise_list, attrs={"class": "form-control", 'placeholder': 'Category'}),
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

        
