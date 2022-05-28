from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def NewsPage(request):
    context ={
    "news": Post,

    }
    return render(request, 'newsukrain/index.html', context)
