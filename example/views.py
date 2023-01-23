from django.core.handlers.asgi import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('Deployed')
