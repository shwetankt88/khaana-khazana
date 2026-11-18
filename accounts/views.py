from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from .forms import SignUpForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipes:home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    user_recipes = user.recipes.all().order_by('-created_at')
    favorites = user.favorites.select_related('recipe').all()
    recipe_count = user_recipes.count()
    avg_rating = user_recipes.aggregate(avg=Avg('reviews__rating'))['avg']
    total_favs_received = sum(r.favorite_count for r in user_recipes)

    return render(request, 'accounts/profile.html', {
        'profile_user': user,
        'user_recipes': user_recipes,
        'favorites': favorites,
        'recipe_count': recipe_count,
        'avg_rating': avg_rating,
        'total_favs_received': total_favs_received,
    })
