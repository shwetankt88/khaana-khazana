from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipe_list, name='list'),
    path('recipes/new/', views.recipe_create, name='create'),
    path('recipes/<slug:slug>/', views.recipe_detail, name='detail'),
    path('recipes/<slug:slug>/edit/', views.recipe_update, name='update'),
    path('recipes/<slug:slug>/delete/', views.recipe_delete, name='delete'),
    path('recipes/<slug:slug>/print/', views.print_recipe, name='print'),
]
