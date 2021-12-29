from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

from contacts.models import Contact

# Create your views here.
def inquiry(request):



    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = user_id = request.POST['user_id']
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already a request about this car')
                return redirect('/cars/'+car_id)

        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name, last_name=last_name, customer_need=customer_need, city=city, 
        state=state, email=email, phone=phone, message=message )

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email


        send_mail(
            'New Car Inquery',
            'You have a new inquery for the car ' + car_title + '. Please login to your admin panel for more info',
            'bcadc555@gmail.com',
            [admin_email],
            fail_silently=False,
        )


        contact.save()

        



        messages.success(request, 'Your request has been submitted successfully, we will contact you shortly')
        return redirect('/cars/'+car_id)


