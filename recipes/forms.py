from django import forms
from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'category', 'description', 'instructions', 'prep_time', 'cook_time', 'servings', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'instructions': forms.Textarea(attrs={'rows': 5}),
        }