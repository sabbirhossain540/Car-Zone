from django.shortcuts import render
from .models import Teams

# Create your views here.

def home(request):
    teams = Teams.objects.all()
    data = {
        'teams': teams
    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Teams.objects.all()
    data = {
        'teams': teams
    }

    return render(request, 'pages/about.html', data)

def contact(request):
    return render(request, 'pages/contact.html')


def services(request):
    return render(request, 'pages/services.html')