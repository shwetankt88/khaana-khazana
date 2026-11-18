from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meal_plans')
    week_start = models.DateField(help_text="Monday of the planned week")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'week_start')
        ordering = ['-week_start']

    def __str__(self):
        return f"{self.user.username}'s plan for week of {self.week_start}"

class MealPlanItem(models.Model):
    DAY_CHOICES = [
        (0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'),
        (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday'),
    ]
    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]

    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE, related_name='items')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    day = models.IntegerField(choices=DAY_CHOICES)
    meal_type = models.CharField(max_length=10, choices=MEAL_CHOICES)

    class Meta:
        ordering = ['day', 'meal_type']

    def __str__(self):
        return f"{self.get_day_display()} {self.meal_type}: {self.recipe.title}"
