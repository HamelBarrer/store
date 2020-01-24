from django.shortcuts import render
from .models import Cart


# Create your views here.
def cart(request):
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart = Cart.objects.get(pk=cart_id)
    else:
        cart = Cart.objects.create(user=user)
    request.session['cart_id'] = cart.id    
    template_name = 'carts/cart.html'
    return render(request, template_name, {

    })
