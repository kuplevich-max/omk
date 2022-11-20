from django.urls import path
from .views import index,products, timetable, products_detail, main
urlpatterns = [
    path('', main),
    path('main/', index, name='main'),
    path('products/', products,name='products'),
    path('timetable/<str:town>', timetable,name='timetable'),
    path('products/<int:pk>',products_detail,name='products_detail')
]