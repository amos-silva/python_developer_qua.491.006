from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Olá Mundo Django , Estamos iniciando uma nova estapa, logo logo estaremos nas Nuvens !!!")