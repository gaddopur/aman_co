from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product

def home(request):
    templates = "home.html"
    products = Product.objects.all().order_by('update')
    context = {'products': products}
    return render(request, templates, context)
