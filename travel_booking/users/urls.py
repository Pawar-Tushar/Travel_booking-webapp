from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, profile_view
from users.forms import LoginForm
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html' , authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', profile_view, name='profile'),
]
