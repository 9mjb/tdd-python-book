from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    # v1
    # return HttpResponse('<html><title>To-Do lists</title></html>')
    # v2
    #if request.method == 'POST':
    #    return HttpResponse(request.POST['item_text'])
    #return render(request, 'home.html')    # (ff templates/home.html)
    # v3                                    # (ff tests.py)
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', '')
    })
