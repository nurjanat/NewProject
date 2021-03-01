from django.urls import path
from .views import *
urlpatterns = [
    path('movies/<int:movie_id>/',movies_view,name='movie'),
    path('comments/',comments_page),
    path('',movies_page,name='home'),
    path('ratings/<int:movie_id>/',ratings_page),

]
