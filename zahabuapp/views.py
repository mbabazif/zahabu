from django.shortcuts import render

from django.shortcuts import render,redirect
from django.conf import settings


def index(request):
    return render(request, 'index.html')
