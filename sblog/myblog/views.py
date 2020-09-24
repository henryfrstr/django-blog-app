from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, PostUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# def home(request):
#     context = {}
#     return render(request, 'myblog/home.html', context)

class HomeView(ListView):
    model = Post
    template_name = "myblog/home.html"
    # ordering = ["-id"]

# class CategoryView(ListView):
#     model = Post
#     template_name = "myblog/category.html"

#     def get_queryset(self):
#         query_set = Post.objects.filter(category=self.kwargs['category'])
        # print(self.category_posts)
        # return  get_object_or_404(Post, category=self.kwargs['category'])
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['category'] = self.category
    #     return context

def CategoryView(request, catg):
    category_posts = Post.objects.filter(category=catg)
    context = {
        'catg': catg,
        'category_posts': category_posts
        }
    return render(request, "myblog/category.html", context)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "myblog/post_detail.html"
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    # def get_object(self):
    #     ik = self.kwargs.get("id")
    #     return get_object_or_404(Post, id=ik)


class AddBlogView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "myblog/add_post.html"
    # fields = "__all__"
    login_url = 'login'
    redirect_field_name = 'redirect_to'


class AddCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    # form_class = PostForm
    template_name = "myblog/add_category.html"
    fields = "__all__"
    login_url = 'login'
    redirect_field_name = 'redirect_to'


class UpdateBlogView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = "myblog/post_update.html"
    login_url = 'login'
    redirect_field_name = 'redirect_to'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "myblog/post_delete.html"
    success_url = reverse_lazy("home")
    login_url = 'login'
    redirect_field_name = 'redirect_to'