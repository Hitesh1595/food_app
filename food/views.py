from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404

from food import models

# to load template
from django.template import loader

# Create your views here.

def main_index(request):
    return HttpResponse("Welcome to main page")

def index(request):
    
    items = models.Item.objects.all()

    # template = loader.get_template('food/index.html')
    context = {
        "items":items,
    }
    print(context)
    return render(request,'food/index.html',context = context)

    # another way to load template
    # return HttpResponse(template.render(context,request))
    

def item(request):
    return HttpResponse("Welcome to item page")
    


def detail(request,pk):
    
    # try:
    #     detail = models.Item.objects.get(pk = pk)
    # except :
    #     raise Http404

    detail = get_object_or_404(models.Item,pk = pk)

    context = {
        'detail':detail
    }
    return render(request,'food/detail.html',context = context)