from django.contrib import admin
from .models import Category, Ingredient, Recipe, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'prep_time', 'cook_time', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [RecipeIngredientInline]

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)