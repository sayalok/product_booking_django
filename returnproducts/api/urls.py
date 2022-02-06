from django.urls import path
from .views import ReturnProductsListView

urlpatterns = [
    path('', ReturnProductsListView.as_view()),
]
