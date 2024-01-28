from django.shortcuts import render
from .models import Product
from django.db.models.functions import Trim


def home(request):
    flowers = Product.objects.order_by('-id')[:3]
    context = {
        'flowers': flowers
    }
    return render(request, 'pages/index.html', context)


def detail(request, flower_id):
    flowers = Product.objects.get(id=flower_id)
    context = {
        'flowers': flowers
    }
    return render(request, 'pages/detail.html', context)


def catalog(request):
    flowers = Product.objects.order_by('-id')
    context = {
        'flowers': flowers
    }
    return render(request, 'pages/catalog.html', context)
