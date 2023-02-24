from .models import Item
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home_screen_view(request):
    print(request.headers)

    my_data = Item.objects.all()
    one_data = Item.objects.get(pk=1)
    context={
        'my_data':my_data,
        'one_data':one_data,
    }
    return render(request, "base.html", context)

def index(request):
    latest_item_list = Item.objects.all()
    return HttpResponse("Hello, world. You're at the items index.")

# def get_data(request):
#     my_data = Item.objects.all()
#     one_data = Item.objects.get(pk=1)
#     context={
#         'my_data' :my_data,
#         'one_data' :one_data,
#     }

#     return render(request, 'get_data.html', context)
