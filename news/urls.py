from django.urls import path
from .views import list_news, news_detail
urlpatterns=[
    path('',list_news,name='list_news'),
    path('<int:category>/', news_detail, name='news_detail'),
]