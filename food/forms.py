from django import forms
from food import models


class ItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        # fields = '__all__'
        fields = ['item_name','item_desc','item_price','item_image']