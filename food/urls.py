from django.urls import path,include

from food import views

urlpatterns = [
    path('',views.index,name = 'index')
]