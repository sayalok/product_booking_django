from django.urls import path

from .views import getProductList

urlpatterns = [
    path('list', getProductList), 
]
