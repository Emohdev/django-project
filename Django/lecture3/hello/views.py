from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def bammy(request):
    return HttpResponse("Hello, bammy!")