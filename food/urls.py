from django.urls import path,include

from food import views

app_name = 'food'

urlpatterns = [
    #food/
    path('',views.index,name = 'index'),

    #food/item/
    path('item/',views.item,name = 'item'),

    #food/1
    path('<int:pk>/',views.detail,name = 'detail')
]