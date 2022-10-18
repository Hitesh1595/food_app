from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length = 255)
    item_desc = models.CharField(max_length = 255)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length = 500,default = "https://cdn-icons-png.flaticon.com/128/1159/1159207.png?ga=GA1.2.729369652.1666116741")

    def __str__(self):
        return self.item_name
