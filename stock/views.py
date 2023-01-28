from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q

from .models import Stock, Category
from .forms import StockForm


def get_stocks(request):
    """View to show all products, includes sorting and search functionality"""

    stocks = Stock.objects.all()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                stocks = stock.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            stocks = stocks.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            stocks = stocks.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query)
            stocks = stocks.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'stocks': stocks,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'stock/stock.html', context)


def stock_detail(request, stock_id):
    """ A view to show individual stock details """

    stock = get_object_or_404(Stock, pk=stock_id)

    context = {
        'stock': stock,
    }

    return render(request, 'stock/stock_detail.html', context)


def add_stock(request):
    """ Add a stock line to the store """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = StockForm(request.POST, request.FILES)
        if form.is_valid():
            stock = form.save()
            return redirect(reverse('stock_detail', args=[stock.id]))
    else:
        form = StockForm()

    template = 'stock/add_stock.html'
    context = {
        'form': form
    }

    return render(request, template, context)


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
