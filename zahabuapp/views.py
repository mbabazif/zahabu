from django.shortcuts import render

from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib import admin
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


def index(request):
    return render(request, 'index.html')

def events(request):
    return render(request, 'events.html')

def about(request):
    return render(request, 'about.html')

def deals(request):
    return render(request, 'deal.html')

def services(request):
    return render(request, 'services.html')

def product(request):
    return render(request, 'side_navbar/product.html')

def household(request):
    return render(request, 'side_navbar/household.html')










