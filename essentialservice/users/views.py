from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def register(request):
    return render(request, 'users/register.html')

def login(request):
    return render(request, 'users/login.html')

def userdashboard(request):
    return render(request, 'users/userdashboard.html')

def edit_profile(request):
    return render(request, 'users/edit_profile.html')

def forgot_password(request):
    return render(request, 'users/forgot_password.html')

def reset_password(request):
    return render(request, 'users/reset_password.html')

def search_service(request):
    return render(request, 'users/search_service.html')

def electrical(request):
    return render(request, 'users/electrical.html')

def plumbing(request):
    return render(request, 'users/plumbing.html')

def cleaning(request):
    return render(request, 'users/cleaning.html')

def dailychores(request):
    return render(request, 'users/dailychores.html')

def records(request):
    return render(request, 'users/records.html')