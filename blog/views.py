from django.shortcuts import render
from django.urls import path, include
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, Blog!")