from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404

# Create your views here.


def index(request):
    return HttpResponse("welcome to index page")
    

def item(request):
    return HttpResponse("welcome to item view")