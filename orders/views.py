from django.shortcuts import render


# Create your views here.
def order(request):
    template_name = 'order/order.html'
    return render(request, template_name, {

    })
