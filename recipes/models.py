from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    icon = models.CharField(max_length=50, blank=True, default='🍽️', help_text="Emoji icon for category")

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='recipes')
    description = models.TextField()
    instructions = models.TextField()
    prep_time = models.PositiveIntegerField(help_text="Prep time in minutes")
    cook_time = models.PositiveIntegerField(help_text="Cook time in minutes")
    servings = models.PositiveIntegerField(default=4)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    is_vegetarian = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'slug': self.slug})

    @property
    def total_time(self):
        return self.prep_time + self.cook_time

    @property
    def favorite_count(self):
        return self.favorited_by.count()

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50, help_text="e.g. 2 cups, 1 tsp")

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} for {self.recipe.title}"

class NutritionInfo(models.Model):
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE, related_name='nutrition')
    calories = models.PositiveIntegerField(default=0, help_text="Per serving")
    protein = models.DecimalField(max_digits=6, decimal_places=1, default=0, help_text="Grams per serving")
    carbs = models.DecimalField(max_digits=6, decimal_places=1, default=0, help_text="Grams per serving")
    fat = models.DecimalField(max_digits=6, decimal_places=1, default=0, help_text="Grams per serving")
    fiber = models.DecimalField(max_digits=6, decimal_places=1, default=0, help_text="Grams per serving")

    class Meta:
        verbose_name = 'Nutrition Info'
        verbose_name_plural = 'Nutrition Info'

    def __str__(self):
        return f"Nutrition for {self.recipe.title}"
