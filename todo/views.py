from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


def get_todo_list(request):
    item = Item.objects.all()
    contents = {
        'item': item
    }
    return render(request, 'todo/todo_list.html', contents)


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.post)
        if form.is_valid():
            form.save
            return redirect('todo')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)
