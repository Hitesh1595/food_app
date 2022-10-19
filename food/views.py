from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404

from food import models
from food import forms 

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
    # print(context)
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

def create_item(request):
    form = forms.ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item_form.html',{'form':form})

def update_item(request,pk):

    item = get_object_or_404(models.Item,pk = pk)

    form = forms.ItemForm(request.POST or None,instance = item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item_form.html',{'form':form,'item':item})

def delete_item(request,pk):
    item = get_object_or_404(models.Item,pk = pk)

    # form = forms.ItemForm(request.POST or None,instance = item)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request,'food/delete_item.html',{'item':item})

