from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
def home_page(request):
    # v1
    # return HttpResponse('<html><title>To-Do lists</title></html>')
    # v2
    #if request.method == 'POST':
    #    return HttpResponse(request.POST['item_text'])
    #return render(request, 'home.html')    # (ff templates/home.html)
    # v3                                    # (ff tests.py)
    #item = Item()
    #item.text = request.POST.get('item_text', '')
    #item.save()
    #return render(request, 'home.html', {
    #    'new_item_text': item.text # request.POST.get('item_text', '')
    #})
    #v4
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list')
    items = Item.objects.all()
    return render(request, 'home.html')
#   #, { 'new_item_text': new_item_text # request.POST.get('item_text', '') })

def view_list(request):
    pass
    items = Item.objects.all()
    return render(request, 'list.html', { 'items': items})


