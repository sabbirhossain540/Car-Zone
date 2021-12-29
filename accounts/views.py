from django.shortcuts import redirect, render
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Password']

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are Logged in Successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Username and Password not match')
            return render(request, 'accounts/login.html')


    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already Exist')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email Already Exist')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    # auth.login(request, user)
                    # messages.success(request, 'You are logged in successfully')
                    # return redirect('dashboard')
                    user.save()
                    messages.success(request, 'You are register successfully')
                    return redirect('login')

        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
        

    else:
        return render(request, 'accounts/register.html')

     

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

    

@login_required(login_url = 'login')
def dashboard(request):
    print(request.user.id)
    user_inquery = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)
    from django.http import HttpResponse
    #return HttpResponse(user_inquery)
    print(user_inquery)
    data = {
        'inqures' : user_inquery,
    }
    return render(request, 'accounts/dashboard.html', data)