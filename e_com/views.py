from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

# Create your views here.
def home(request):
    product = Product.objects.all().filter(is_available=True)
    context ={
        'product':product
    }
    return render(request,"home.html",context)