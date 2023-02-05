from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from stock.models import Stock


def basket_contents(request):

    basket_items = []
    total = 0
    stock_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            stock = get_object_or_404(Stock, pk=item_id)
            total += item_data * stock.price
            stock_count += item_data
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'stock': stock,
            })

    grand_total = total

    context = {
        'basket_items': basket_items,
        'total': total,
        'stock_count': stock_count,
        'grand_total': grand_total,
    }

    return context
