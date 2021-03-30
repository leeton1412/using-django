from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class meta:
        model = Item
        fields = ['name', 'done']
