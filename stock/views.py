from django.shortcuts import render

from .models import Stock, Category


def get_stocks(request):
    """View to show all products, includes sorting and search functionality"""

    stocks = Stock.objects.all()

    context = {
        'stocks': stocks
    }

    return render(request, 'stock/stock.html', context)
