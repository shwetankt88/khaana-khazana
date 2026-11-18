from django.contrib import admin
from .models import Category, Ingredient, Recipe, RecipeIngredient, NutritionInfo

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class NutritionInfoInline(admin.StackedInline):
    model = NutritionInfo
    extra = 0
    max_num = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'difficulty', 'prep_time', 'cook_time', 'created_at')
    list_filter = ('category', 'difficulty', 'is_vegetarian', 'is_vegan', 'is_gluten_free', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [RecipeIngredientInline, NutritionInfoInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'icon')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Ingredient)
