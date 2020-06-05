from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('products',views.all_products, name='all_products'),
]