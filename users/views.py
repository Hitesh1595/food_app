from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from users import forms


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get("username")
            messages.success(request,f"{username} has been created successfuly")

            return redirect('login')
    else:
        form = forms.RegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profilepage(request):
    return render(request,'users/profilepage.html')
