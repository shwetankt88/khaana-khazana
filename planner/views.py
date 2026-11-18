from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from recipes.models import Recipe
from .models import MealPlan, MealPlanItem
from datetime import date, timedelta
from collections import defaultdict


@login_required
def meal_planner(request):
    # Get current week's Monday
    today = date.today()
    monday = today - timedelta(days=today.weekday())

    week_offset = int(request.GET.get('week', 0))
    monday = monday + timedelta(weeks=week_offset)

    meal_plan, created = MealPlan.objects.get_or_create(user=request.user, week_start=monday)

    # Build grid data
    days = [(i, (monday + timedelta(days=i)).strftime('%a %d %b')) for i in range(7)]
    meal_types = ['breakfast', 'lunch', 'dinner', 'snack']

    grid = {}
    for item in meal_plan.items.select_related('recipe'):
        grid[(item.day, item.meal_type)] = item

    recipes = Recipe.objects.all().order_by('title')

    return render(request, 'planner/meal_planner.html', {
        'meal_plan': meal_plan,
        'days': days,
        'meal_types': meal_types,
        'grid': grid,
        'recipes': recipes,
        'week_offset': week_offset,
        'monday': monday,
    })


@login_required
def add_meal(request, day, meal_type, recipe_slug):
    today = date.today()
    monday = today - timedelta(days=today.weekday())
    week_offset = int(request.GET.get('week', 0))
    monday = monday + timedelta(weeks=week_offset)

    meal_plan, _ = MealPlan.objects.get_or_create(user=request.user, week_start=monday)
    recipe = get_object_or_404(Recipe, slug=recipe_slug)

    MealPlanItem.objects.update_or_create(
        meal_plan=meal_plan, day=day, meal_type=meal_type,
        defaults={'recipe': recipe}
    )
    return redirect(f'/planner/?week={week_offset}')


@login_required
def remove_meal(request, item_id):
    item = get_object_or_404(MealPlanItem, pk=item_id, meal_plan__user=request.user)
    week_offset = request.GET.get('week', 0)
    item.delete()
    return redirect(f'/planner/?week={week_offset}')


@login_required
def shopping_list(request):
    today = date.today()
    monday = today - timedelta(days=today.weekday())
    week_offset = int(request.GET.get('week', 0))
    monday = monday + timedelta(weeks=week_offset)

    try:
        meal_plan = MealPlan.objects.get(user=request.user, week_start=monday)
        items = meal_plan.items.select_related('recipe').all()
    except MealPlan.DoesNotExist:
        items = []

    # Aggregate ingredients
    ingredients = defaultdict(list)
    for item in items:
        for ri in item.recipe.recipe_ingredients.select_related('ingredient').all():
            ingredients[ri.ingredient.name].append(ri.quantity)

    return render(request, 'planner/shopping_list.html', {
        'ingredients': dict(ingredients),
        'monday': monday,
        'week_offset': week_offset,
    })
