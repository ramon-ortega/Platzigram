"""Posts Views"""

# Django
from django.shortcuts import render
from django.http import HttpResponse

def list_posts(requets):
    """Muestra la lista de posts"""
    return HttpResponse('Muestra los posts')


