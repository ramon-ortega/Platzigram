"""Platzigram views."""

#Django
from django.http import HttpResponse, JsonResponse
import json

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

def sol_numeros(request):
    """Esta es la solucion del profe al reto"""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_numbers = sorted(numbers)
    data = {
        'status' : 'ok',
        'sorted numbers' : sorted_numbers,
        'message' : 'Integers sorted succesfuly'
    }
    return HttpResponse(json.dumps(data=4),
     content_type="application/json")

def say_hi(request, name, age):
    """ Saluda a la persona y le menciona su nombre"""
    if age < 18:
        message = 'Ups {}, no puedes estar aqui'.format(name)
    else:
        message = 'Bienvenido a Platzigram {}'.format(name)
    return HttpResponse(message)