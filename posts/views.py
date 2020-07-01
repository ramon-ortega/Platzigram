"""Posts Views"""

# Django
from django.shortcuts import render
from django.http import HttpResponse

def list_posts(requets):
    """Show the posts list"""
    return HttpResponse('Aqui va a la lista de posts')