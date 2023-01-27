from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import Stock, Category
from .forms import StockForm


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


def edit_stock(request, stock_id):
    """ Edit a stock in the store """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    stock = get_object_or_404(Stock, pk=stock_id)
    if request.method == 'POST':
        form = StockForm(request.POST, request.FILES, instance=stock)
        if form.is_valid():
            form.save()
            return redirect(reverse('stock_detail', args=[stock.id]))
    else:
        form = StockForm(instance=stock)

    template = 'stock/edit_stock.html'
    context = {
        'form': form,
        'stock': stock
    }

    return render(request, template, context)


def delete_stock(request, stock_id):
    """ Delete a stock from the store """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    stock = get_object_or_404(Stock, pk=stock_id)
    stock.delete()
    return redirect(reverse('stocks'))
