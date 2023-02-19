from django.shortcuts import render, redirect, reverse, get_object_or_404


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
            review.save()
            return redirect(reverse('review'))
    else:
        form = ReviewForm()

    template = 'testimonials/review.html'
    context = {
        'form': form
    }

    return render(request, template, context)


# def approve_review(request, review_id):

#     reviews = Review.objects.get(Review, pk=review_id)
#     reviews.approved = True
#     return redirect(reverse('review'))


def delete_review(request, review_id):
    """ Delete a stock from the store """
    # if not request.user.is_superuser:
    #     return redirect(reverse('home'))

    reviews = get_object_or_404(Review, pk=review_id)
    reviews.delete()
    return redirect(reverse('review'))
