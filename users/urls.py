from users.views import LoginView, LogoutView, RegisterView, ProfileView, EmailConfirmView, generate_new_password
from django.urls import path

from users.apps import UsersConfig


app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('email_confirm_form/', EmailConfirmView.as_view(), name='email_confirm_form'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),
]