from django.urls import path
from .views import ProductDetailView, ProductSerchView

app_name = 'products'

urlpatterns = [
    path('search', ProductSerchView.as_view(), name='search'),
    path('<slug:slug>', ProductDetailView.as_view(), name='product'),
]
