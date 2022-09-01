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

