from django.shortcuts import render

from basket.contexts import basket_contents
from stock.models import Stock
from .forms import OrderForm
from .models import Order, OrderLineItem
from user_details.forms import UserDetailsForm
from user_details.models import UserDetails


def checkout(request):

    if request.method == 'POST':
        basket = request.session.get('basket', {})

    form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

    order_form = OrderForm(form_data)

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
