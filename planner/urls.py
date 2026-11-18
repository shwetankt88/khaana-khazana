from django.urls import path
from . import views

app_name = 'planner'

urlpatterns = [
    path('', views.meal_planner, name='meal_planner'),
    path('add/<int:day>/<str:meal_type>/<slug:recipe_slug>/', views.add_meal, name='add_meal'),
    path('remove/<int:item_id>/', views.remove_meal, name='remove_meal'),
    path('shopping-list/', views.shopping_list, name='shopping_list'),
]
