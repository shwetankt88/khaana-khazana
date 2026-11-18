from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from recipes.models import Recipe
from .forms import ReviewForm

@login_required
def add_review(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.recipe = recipe
            # Check if user already reviewed, update if exists
            existing_review = recipe.reviews.filter(user=request.user).first()
            if existing_review:
                existing_review.rating = review.rating
                existing_review.comment = review.comment
                existing_review.save()
            else:
                review.save()
    return redirect(recipe.get_absolute_url())