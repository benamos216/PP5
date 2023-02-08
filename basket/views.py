from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, reverse
from stock.models import Stock


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    stock = get_object_or_404(Stock, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    stock = get_object_or_404(Stock, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ Remove the item from the shopping bag """

    try:
        stock = get_object_or_404(Stock, pk=item_id)

        basket = request.session.get('basket', {})
        basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)