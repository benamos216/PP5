from django.shortcuts import render, redirect, reverse
from django.conf import settings

from basket.contexts import basket_contents
from stock.models import Stock
from .forms import OrderForm
from .models import Order, OrderLineItem
from profiles.forms import UserProfileForm
from profiles.models import UserProfile

import stripe
import json


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

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
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    stock = Stock.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            stock=stock,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    order.delete()
                    return redirect(reverse('view_basket.html'))

            request.session['save_info'] = 'save_info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
    else:
        basket = request.session.get('basket', {})
        if not basket:
            return redirect(reverse('stocks'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'first_name': profile.user.first_name,
                    'last_name': profile.user.last_name,
                    'email': profile.user.email,
                    'phone_number': profile.user.default_phone_number,
                    'postcode': profile.user.default_postcode,
                    'town_or_city': profile.user.default_town_or_city,
                    'street_address1': profile.user.default_street_address1,
                    'street_address2': profile.user.default_street_address2,
                    'county': profile.user.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
