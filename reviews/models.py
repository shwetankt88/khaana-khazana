from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], help_text="Rating from 1 to 5")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('recipe', 'user') # Ek user ek recipe par ek hi review de sakta hai

    def __str__(self):
        return f"{self.user.username}'s review on {self.recipe.title} - {self.rating}★"