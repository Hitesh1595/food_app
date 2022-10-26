from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404

from food import models
from food import forms 

# to load template
from django.template import loader

# import list view (generic)
from django.views.generic.list import ListView
# import detail view
from django.views.generic.detail import DetailView
# import create
from django.views.generic.edit import CreateView

# Create your views here.

def main_index(request):
    return HttpResponse("Welcome to main page")
      
#NOTE
# fuctional based function view of list item
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

# list view of item(index)
class IndexClassView(ListView):
    model = models.Item
    template_name = 'food/index.html'
    context_object_name = 'items'
    
    # reverse the list
    def get_queryset(self, *args, **kwargs):
        qs = super(IndexClassView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs
    

def item(request):
    return HttpResponse("Welcome to item page")
    
# NOTE
# function based vies of item descriptions
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

class FoodDetail(DetailView):
    model = models.Item
    template_name = 'food/detail.html'
    context_object_name = 'detail'

# function based view
def create_item(request):
    form = forms.ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item_form.html',{'form':form})

# class based view for create item
class CreateItem(CreateView):
    model = models.Item
    fields = ['item_name','item_desc','item_price','item_image']

     # if form class specific fiels are not used
    # form_class = forms.ItemForm
    template_name = 'food/item_form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)




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

