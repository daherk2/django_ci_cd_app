from django.shortcuts import render
from django.http import request, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("OKOK")

def teste(request):
    return HttpResponse("OK - TESTE")
