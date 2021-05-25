from django.shortcuts import render
from django.http import HttpResponse

#<a href='/about/>About</a>
def index(request):
    return HttpResponse("Rango says hey there partner! http://127.0.0.1:8000/rango/about/ ")

def about(request):
    return HttpResponse("Rango says here is the about page. http://127.0.0.1:8000/rango/")

