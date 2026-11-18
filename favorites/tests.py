from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from recipes.models import Recipe
from .models import Favorite


class FavoriteModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('chef', 'c@t.com', 'pass1234')
        self.recipe = Recipe.objects.create(
            title='Dal', slug='dal', author=self.user,
            description='Lentils', instructions='Cook',
            prep_time=10, cook_time=20, servings=4
        )

    def test_create_favorite(self):
        fav = Favorite.objects.create(user=self.user, recipe=self.recipe)
        self.assertIn('chef', str(fav))
        self.assertIn('Dal', str(fav))

    def test_unique_together(self):
        Favorite.objects.create(user=self.user, recipe=self.recipe)
        with self.assertRaises(Exception):
            Favorite.objects.create(user=self.user, recipe=self.recipe)


class FavoriteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('chef', 'c@t.com', 'pass1234')
        self.recipe = Recipe.objects.create(
            title='Dal', slug='dal', author=self.user,
            description='Lentils', instructions='Cook',
            prep_time=10, cook_time=20, servings=4
        )

    def test_toggle_requires_login(self):
        resp = self.client.get(reverse('favorites:toggle', args=['dal']))
        self.assertEqual(resp.status_code, 302)

    def test_toggle_creates_favorite(self):
        self.client.login(username='chef', password='pass1234')
        resp = self.client.get(reverse('favorites:toggle', args=['dal']))
        self.assertEqual(Favorite.objects.count(), 1)

    def test_toggle_removes_favorite(self):
        self.client.login(username='chef', password='pass1234')
        Favorite.objects.create(user=self.user, recipe=self.recipe)
        self.client.get(reverse('favorites:toggle', args=['dal']))
        self.assertEqual(Favorite.objects.count(), 0)

    def test_favorite_list_requires_login(self):
        resp = self.client.get(reverse('favorites:list'))
        self.assertEqual(resp.status_code, 302)

    def test_favorite_list_logged_in(self):
        self.client.login(username='chef', password='pass1234')
        resp = self.client.get(reverse('favorites:list'))
        self.assertEqual(resp.status_code, 200)
