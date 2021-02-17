from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from .models import *
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template.loader import render_to_string

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .models import Movies

from .forms import *
from . tokens import account_activation_token


# Create your views here.

def movies_page(request):
    movies = Movies.objects.all()
    return render(request,'movies/movies.html',{'movies':movies})




def register_page(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account. '
            message = render_to_string('products/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to comlete the registrations')

