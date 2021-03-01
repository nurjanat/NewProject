from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
from .filters import *


# Create your views here.

def movies_page(request):
    movies = Movies.objects.all()
    filters = MoviesFilter(request.GET, queryset=movies)
    movies = filters.qs
    return render(request,'movies/movies.html',{'movies':movies,'filters':filters})



def comments_page(request):
    comments = Comments.objects.all()
    return render(request,'movies/comments.html',{'comments':comments})



def movies_view(request,movie_id):
    movies = Movies.objects.get(id=movie_id)
    rates = movies.rate_set.all()
    form1 = RatingsForm(initial={'film': movies})
    total = 0
    len_rates = len(rates)
    comments = movies.comments_set.all()
    form = CommentsForm(initial={'film': movies,})
    for i in rates:
        total += i.rate
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        form1 = RatingsForm(request.POST)

        if form.is_valid() and form1.is_valid():
            if 0 <= form1.cleaned_data['rate'] <= 5:
                form.save()
                form1.save()
            else:
                return HttpResponse('NOT OK RATE FOR FILM')
    try:
        context = {"movie":movies,'form':form,'comments':comments,'rates':round(total/len_rates,1), 'form1': form1}
    except ZeroDivisionError:
        context = {'rates': 0, 'form1': form1,'movie':movies,'comments':comments,}

    return render(request,'movies/details_movies.html',context)


def ratings_page(request,movie_id):
    movie = Movies.objects.get(id=movie_id)
    rates = movie.rate_set.all()
    form = RatingsForm(initial={'film': Movies})
    total = 0
    len_rates = len(rates)
    for i in rates:
        total += i.rate
    if request.method  == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            if 0<=form.cleaned_data['rate'] <=5:
                form.save()
            else:
                return HttpResponse('NOT OK RATE FOR FILM')
    try:
        context = {'rates':round(total/len_rates,1),'form':form}
    except ZeroDivisionError:
        context = {'rates':0,'form':form}
    return render(request,'movies/rating_page.html',{'form':form,})





