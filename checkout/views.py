from django.shortcuts import render


def checkout(request):

    template = 'checkout/checkout.html'
    context = {
        
    }

    return render(request, template, context)
