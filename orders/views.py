from django.shortcuts import render
from .utils import get_or_create_order, breadcrumb
from carts.utils import get_or_create_cart
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def order(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)
    template_name = 'order/order.html'
    return render(request, template_name, {
        'cart': cart,
        'order': order,
        'breadcrumb': breadcrumb()
    })
