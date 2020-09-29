from django.shortcuts import redirect, render
from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html')


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


def view_list(request, list_id): # list_id is arg from URL regex capture group (+d)
    list = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list)
    return render(request, 'list.html', {'list': list, 'items': items})


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
