from django.shortcuts import render, redirect
from .models import Cart
from products.models import Product
from .utils import get_or_create_cart


# Create your views here.
def cart(request):
    cart = get_or_create_cart(request)
    template_name = 'carts/cart.html'
    return render(request, template_name, {
        'cart': cart
    })


def add(request):
    cart = get_or_create_cart(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))

    cart.products.add(product)
    template_name = 'carts/add.html'
    return render(request, template_name, {
        'product': product
    })


def remove(request):
    cart = get_or_create_cart(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))

    cart.products.remove(product)

    return redirect('carts:cart')
