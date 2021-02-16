from django.urls import path
from .views import *
urlpatterns = [
    path('movies/',movies_page),
    path('registers/', register_page, ),
]