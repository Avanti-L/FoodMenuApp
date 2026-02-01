from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def index(request):
    # Fetch data from the database
    item_list = Item.objects.all()
    # Create context to pass data to template
    context = {
        'item_list': item_list
    }
    # Passing the context object to template
    return render(request, "myapp/index.html", context)

def detail(request, id):
    item = Item.objects.get(id=id)
    context = {
        'item': item
    }
    return render(request, "myapp/detail.html", context)


def item(request):
    return HttpResponse("<h1>This is an item view</h1>")