from django.shortcuts import render
from .models import Item
# Create your views here.


def get_todo_list(request):
    item = Item.objects.all()
    contents = {
        'item': item
    }
    return render(request, 'todo/todo_list.html', contents)
