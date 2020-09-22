from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, PostUpdateForm
from django.urls import reverse_lazy


# def home(request):
#     context = {}
#     return render(request, 'myblog/home.html', context)

class HomeView(ListView):
    model = Post
    template_name = "myblog/home.html"
    # ordering = ["-id"]


class PostDetailView(DetailView):
    model = Post
    template_name = "myblog/post_detail.html"

    # def get_object(self):
    #     ik = self.kwargs.get("id")
    #     return get_object_or_404(Post, id=ik)


class AddBlogView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "myblog/add_post.html"
    # fields = "__all__"


class UpdateBlogView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = "myblog/post_update.html"


class PostDeleteView(DeleteView):
    model = Post
    template_name = "myblog/post_delete.html"
    success_url = reverse_lazy("home")
