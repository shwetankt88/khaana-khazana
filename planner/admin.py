from django.contrib import admin
from .models import MealPlan, MealPlanItem


class MealPlanItemInline(admin.TabularInline):
    model = MealPlanItem
    extra = 1


@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ['user', 'week_start', 'created_at']
    list_filter = ['week_start']
    inlines = [MealPlanItemInline]
