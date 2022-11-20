from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import ProductCategory, Product


def index(request):
    return render(request,'index1.html',{})


def main(request):
    return HttpResponseRedirect(reverse_lazy('main'))


def products(request):
    products = ProductCategory.objects.all()
    return render(request,'products.html',{'products':products})


def timetable(request, town):
    return render(request,'timetable.html',{'town': town})


def products_detail(request,pk):
    products = Product.objects.filter(category=pk)
    title = ProductCategory.objects.get(pk=pk).title
    categories = ProductCategory.objects.all()
    context = {
        'products': products,
        'title': title,
        'categories': categories
    }
    return render(request,'products_detail.html', context)


