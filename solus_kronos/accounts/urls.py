from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LoginView
from .views import CustomLoginView  # Substitua 'CustomLoginView' pelo nome da sua view personalizada
from django.contrib.auth.views import LogoutView
from .views import edit_user
from .views import change_password,login,admin_redirect,custom_login_redirect





urlpatterns = [
    path('register/', views.register, name='register'),
    path('old_login/', CustomLoginView.as_view(), name='login_login'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('edit/', edit_user, name='edit_user'),
    path('mudar_senha/', change_password, name='mudar_senha'),
    path('login/', login, name='login'),
    path('admin-redirect/', views.admin_redirect, name='admin_redirect'),
    path('custom-login-redirect/', custom_login_redirect, name='custom_login_redirect'),



]
