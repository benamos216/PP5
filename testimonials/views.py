from django.shortcuts import render, redirect, reverse


from .models import Review
from .forms import ReviewForm


def review(request):

    reviews = Review.objects.all()
    template = 'testimonials/testimonials.html'

    context = {
        "reviews": reviews,
    }

    return render(request, template, context)


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            review = form.save(commit=False)
            # review.save()
            return redirect(reverse('review'))
    else:
        form = ReviewForm()

    template = 'testimonials/review.html'
    context = {
        'form': form
    }

    return render(request, template, context)
