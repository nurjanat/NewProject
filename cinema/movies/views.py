from django.contrib.auth import authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from .models import *
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .models import Movies

from .forms import *
from .tokens import account_activation_token


# Create your views here.

def movies_page(request):
    movies = Movies.objects.all()
    return render(request, 'movies/movies.html', {'movies': movies})


def register_page(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

    context = {'form':form}
    return render (request,'movies/register.html',context)




def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return HttpResponse ('ВЫ УСПЕШНО ВОШЛИ')
    return render(request, 'movies/sign_in.html')


def comments_page(request):
    comments = Comments.objects.all()
    return render(request, 'movies/comments.html', {'comments': comments})
