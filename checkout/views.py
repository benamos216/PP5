from django.shortcuts import render

from basket.contexts import basket_contents
from stock.models import Stock


def checkout(request):

    if request.method == 'POST':
        basket = request.session.get('basket', {})

    template = 'checkout/checkout.html'
    context = {

    }

    return render(request, template, context)
