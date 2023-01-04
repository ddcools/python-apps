from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
  return render(request, 'home.html', {'name': "Gananv", 'status': 'TEST'})

def welcome_user(request):
  return HttpResponse("Welcome To User Ground")

def logout(request):
  return HttpResponse("You have logged out of the application")