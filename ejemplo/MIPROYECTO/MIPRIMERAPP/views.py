from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hola mundo, estas en la pagina de la app")

def ABOUTA(requets):
    return render(request, "MIPRIMERAAP/about.html")