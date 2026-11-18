from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'category', 'description', 'instructions', 'prep_time',
                  'cook_time', 'servings', 'difficulty', 'image',
                  'is_vegetarian', 'is_vegan', 'is_gluten_free']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recipe title...'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Brief description...'}),
            'instructions': forms.Textarea(attrs={'rows': 6, 'class': 'form-control', 'placeholder': 'Step by step instructions...'}),
            'prep_time': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'cook_time': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'servings': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'difficulty': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
