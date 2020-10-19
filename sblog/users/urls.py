from django.urls import path
from .views import UserRegisterView, UserEditView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/change-password-done.html'), name='password_change_done'),
]
