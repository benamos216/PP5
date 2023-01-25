from django.shortcuts import render, get_object_or_404

from .models import Stock, Category


def get_stocks(request):
    """View to show all products, includes sorting and search functionality"""

    stocks = Stock.objects.all()

    context = {
        'stocks': stocks
    }

    return render(request, 'stock/stock.html', context)


def stock_detail(request, stock_id):
    """ A view to show individual stock details """

    stock = get_object_or_404(Stock, pk=stock_id)

    context = {
        'stock': stock,
    }

    return render(request, 'stock/stock_detail.html', context)
