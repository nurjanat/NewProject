from django.urls import path

from .views import *
from django.contrib.auth import views as auth_views
from .forms import *
urlpatterns = [
    path('registers/', register_page, name='sign_up'),
    path('login/', sign_in, name='sign_in'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/reset_password.html'),
         name='reset_password'),
    path('reset_password_done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/reset_password_done.html'),
         name='password_reset_done'),
]


