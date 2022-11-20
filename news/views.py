from django.shortcuts import render
from .models import News, ListCategory


def list_news(request):
    categories = ListCategory.objects.all()
    news = News.objects.all()
    return render(request,'list_news.html', {'news': news, 'categories': categories})


def news_detail(request, category):
    categories = ListCategory.objects.all()
    news = News.objects.filter(category=category)
    return render(request, 'news_detail.html', {'news': news, 'categories': categories})

# Create your views here.
