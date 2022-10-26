from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse

# Create your models here.

class Item(models.Model):

    user_name = models.ForeignKey(User,on_delete = models.CASCADE,default = 1)
    item_name = models.CharField(max_length = 255)
    item_desc = models.CharField(max_length = 255)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length = 500,default = "https://cdn-icons-png.flaticon.com/128/1159/1159207.png?ga=GA1.2.729369652.1666116741")

    def __str__(self):
        return self.item_name
    
    ''' when item is create this method automatically
            route to (food/pk) specific item page 

            it calls the detail from url and pass unique pk
            
    '''
    def get_absolute_url(self):
        return reverse("food:detail",kwargs = {"pk":self.pk})
