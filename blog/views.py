from django.shortcuts import render
from django
# Create your views here.
def index(request):
    return HttpResponse("Hello, Blog!")