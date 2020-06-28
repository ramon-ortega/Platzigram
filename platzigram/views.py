"""Platzigram views."""

#Django
from django.http import HttpResponse, JsonResponse

#Utilities
from datetime import datetime

def hello_world(request):
    """Return a greeting."""
    return HttpResponse('Hello, World!')

def hi(request):
    """Hi."""
    #import pdb; pdb.set_trace() Este es un debugger
    return HttpResponse('hola, la hora en el servidor es {}'.format(
        datetime.now().strftime('son las %H:%M del dia %e de %B del %Y')))

def numeros(request):
    """Este es un reto que recibe numeros desde la url del navegador, se ordenan y se regresan en formato JSON"""
    numbers = request.GET['numbers']
    number_list = sorted(numbers.split(','))
    print(number_list)
    return JsonResponse({"sorted numbers" : number_list})