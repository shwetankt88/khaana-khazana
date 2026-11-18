from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from recipes.models import Recipe
from .models import Favorite

@login_required
def toggle_favorite(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    favorite, created = Favorite.objects.get_or_create(user=request.user, recipe=recipe)
    if not created:
        favorite.delete() # Agar pehle se favorite hai toh hata do (Toggle)
    return redirect(recipe.get_absolute_url())