from django.urls import path
from . import views

app_name = 'favorites'

urlpatterns = [
    path('recipe/<slug:slug>/favorite/', views.toggle_favorite, name='toggle'),
]