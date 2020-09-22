from django.urls import path
from .views import HomeView, PostDetailView, AddBlogView, UpdateBlogView, PostDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('add/', AddBlogView.as_view(), name='add-blog'),
    path('post/edit/<int:pk>', UpdateBlogView.as_view(), name='edit-blog'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='delete-blog'),
]
