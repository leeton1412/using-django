from django.shortcuts import render, redirect
from .models import Item
# Create your views here.


def get_todo_list(request):
    item = Item.objects.all()
    contents = {
        'item': item
    }
    return render(request, 'todo/todo_list.html', contents)


def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('id_name')
        done = 'id_done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('todo')
    return render(request, 'todo/add_item.html')
