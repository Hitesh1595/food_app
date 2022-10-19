from django.urls import path,include

from food import views

app_name = 'food'

urlpatterns = [
    #food/
    path('',views.index,name = 'index'),

    #food/item/
    path('item/',views.item,name = 'item'),

    #food/1
    path('<int:pk>/',views.detail,name = 'detail'),
    # create item
    path('add',views.create_item,name = 'create_item'),
    # update item
    path('update/<int:pk>/',views.update_item,name = 'update_item'),
    #delete
    path('delete/<int:pk>/',views.delete_item,name = 'delete_item')
]