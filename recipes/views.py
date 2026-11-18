from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.db.models import Q, Avg, Count
from .models import Recipe, Category, NutritionInfo
from .forms import RecipeForm
from reviews.forms import ReviewForm
from favorites.models import Favorite


def home(request):
    recipes = Recipe.objects.all().order_by('-created_at')[:6]
    popular = Recipe.objects.annotate(fav_count=Count('favorited_by')).order_by('-fav_count')[:3]
    categories = Category.objects.all()
    return render(request, 'recipes/home.html', {
        'recipes': recipes,
        'popular': popular,
        'categories': categories,
    })


def recipe_list(request):
    recipes = Recipe.objects.all().order_by('-created_at')

    query = request.GET.get('q')
    if query:
        recipes = recipes.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(recipe_ingredients__ingredient__name__icontains=query)
        ).distinct()

    category_slug = request.GET.get('category')
    if category_slug:
        recipes = recipes.filter(category__slug=category_slug)

    difficulty = request.GET.get('difficulty')
    if difficulty:
        recipes = recipes.filter(difficulty=difficulty)

    # Dietary filters
    if request.GET.get('vegetarian'):
        recipes = recipes.filter(is_vegetarian=True)
    if request.GET.get('vegan'):
        recipes = recipes.filter(is_vegan=True)
    if request.GET.get('gluten_free'):
        recipes = recipes.filter(is_gluten_free=True)

    # Max cook time filter
    max_time = request.GET.get('max_time')
    if max_time:
        try:
            recipes = recipes.filter(cook_time__lte=int(max_time))
        except ValueError:
            pass

    # Sorting
    sort = request.GET.get('sort', 'newest')
    if sort == 'oldest':
        recipes = recipes.order_by('created_at')
    elif sort == 'quickest':
        recipes = recipes.order_by('cook_time')
    elif sort == 'rated':
        recipes = recipes.annotate(avg_r=Avg('reviews__rating')).order_by('-avg_r')
    elif sort == 'popular':
        recipes = recipes.annotate(fav_count=Count('favorited_by')).order_by('-fav_count')

    categories = Category.objects.all()
    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes,
        'categories': categories,
        'query': query,
        'selected_category': category_slug,
        'selected_difficulty': difficulty,
        'selected_sort': sort,
    })


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    reviews = recipe.reviews.all().order_by('-created_at')
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']

    user_favorited = False
    if request.user.is_authenticated:
        user_favorited = Favorite.objects.filter(user=request.user, recipe=recipe).exists()

    # Related recipes (same category, excluding current)
    related = Recipe.objects.filter(category=recipe.category).exclude(pk=recipe.pk)[:3] if recipe.category else Recipe.objects.none()

    nutrition = getattr(recipe, 'nutrition', None)
    review_form = ReviewForm()
    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'reviews': reviews,
        'avg_rating': avg_rating,
        'user_favorited': user_favorited,
        'review_form': review_form,
        'related': related,
        'nutrition': nutrition,
    })


@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            base_slug = slugify(recipe.title)
            slug = base_slug
            counter = 1
            while Recipe.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            recipe.slug = slug
            recipe.save()
            return redirect(recipe.get_absolute_url())
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form, 'action': 'Create'})


@login_required
def recipe_update(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if recipe.author != request.user:
        return redirect('recipes:detail', slug=recipe.slug)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect(recipe.get_absolute_url())
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {'form': form, 'action': 'Update'})


@login_required
def recipe_delete(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if recipe.author == request.user:
        if request.method == 'POST':
            recipe.delete()
            return redirect('recipes:home')
    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})


def print_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    nutrition = getattr(recipe, 'nutrition', None)
    return render(request, 'recipes/print_recipe.html', {
        'recipe': recipe,
        'nutrition': nutrition,
    })
