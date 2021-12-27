from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render

from cars.models import Car

# Create your views here.
def cars(request):
    all_cars = Car.objects.order_by('-created_date')
    paginator = Paginator(all_cars, 3)
    page = request.GET.get('page')
    page_cars = paginator.get_page(page)

    data = {
        'all_cars' : page_cars,
    }
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    data = {
        'single_car' : single_car,
    }
    return render(request, 'cars/car_detail.html', data)