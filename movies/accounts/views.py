from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def register_page(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

    context = {'form':form}
    return render(request,'movies/register.html',context)


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, usernsme=username, password=password)
        login(request, user)
    return render(request, 'movies/sign_in.html')



