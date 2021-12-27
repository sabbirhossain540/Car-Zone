from django.shortcuts import render
from .models import Teams
from cars.models import Car

# Create your views here.

def home(request):
    teams = Teams.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars

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