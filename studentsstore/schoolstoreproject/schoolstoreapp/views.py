from django.contrib.auth.models import User, auth
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def home(request):
    # Your home page logic here
    return render(request, 'home.html')
def base(request):
    # Your home page logic here
    return render(request, 'base.html')

def orderconfirmation(request):
    # Your home page logic here
    return render(request, 'orderconfirmation.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('newpage')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,"login.html")


# def registration(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']  # Fix variable name here
#
#         if password == confirm_password:
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, "Username already taken")
#                 return redirect('registration')
#             elif User.objects.filter(email=email).exists():
#                 messages.error(request, "Email already taken")
#                 return redirect('registration')
#             else:
#                 user=User.objects.create_user(username=username, password=password, first_name=first_name,
#                                                 last_name=last_name, email=email)
#                 user.save()
#                 print("user created")
#                 messages.success(request, "Registration successful. You can now log in.")
#                 return redirect('login')
#         else:
#             messages.error(request, "Passwords do not match")
#             return redirect('registration')
#
#     return render(request, "registration.html")
def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken")
                return redirect('registration')
            else:
                user=User.objects.create_user(username=username, password=password, first_name=first_name,last_name=last_name, email=email)
                user.save()
                messages.success(request, "Registration successful. You can now log in.")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('registration')

    return render(request, "registration.html")


def newpage(request):
    context = {
        'is_newpage': True,
    }
    return render(request, "newpage.html",context)

def department_wikipedia(request, department):
    # Implement redirection to Wikipedia here
    return render(request, "home.html")