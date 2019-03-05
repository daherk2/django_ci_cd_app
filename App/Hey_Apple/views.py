from django.shortcuts import render
from http import request, HttpResponse

# Create your views here.
def index(request):
    returHttpResponse("OKOK")

def teste(request):
    return HttpResponse("OK - TESTE")
