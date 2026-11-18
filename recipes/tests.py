from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Recipe, Category, Ingredient, RecipeIngredient, NutritionInfo


class CategoryModelTest(TestCase):
    def test_str(self):
        cat = Category.objects.create(name='Indian', slug='indian', icon='🍛')
        self.assertEqual(str(cat), 'Indian')


class RecipeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('chef', 'chef@test.com', 'pass1234')
        self.cat = Category.objects.create(name='Indian', slug='indian')
        self.recipe = Recipe.objects.create(
            title='Dal Tadka', slug='dal-tadka', author=self.user,
            category=self.cat, description='Delicious lentils',
            instructions='Cook dal', prep_time=10, cook_time=30,
            servings=4, difficulty='easy', is_vegetarian=True
        )

    def test_str(self):
        self.assertEqual(str(self.recipe), 'Dal Tadka')

    def test_total_time(self):
        self.assertEqual(self.recipe.total_time, 40)

    def test_get_absolute_url(self):
        self.assertEqual(self.recipe.get_absolute_url(), '/recipes/dal-tadka/')

    def test_favorite_count(self):
        self.assertEqual(self.recipe.favorite_count, 0)


class NutritionInfoTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('chef', 'chef@test.com', 'pass1234')
        self.recipe = Recipe.objects.create(
            title='Rice', slug='rice', author=self.user,
            description='Plain rice', instructions='Boil',
            prep_time=5, cook_time=20, servings=2
        )

    def test_nutrition(self):
        n = NutritionInfo.objects.create(recipe=self.recipe, calories=200, protein=4, carbs=45, fat=1)
        self.assertEqual(str(n), 'Nutrition for Rice')


class RecipeViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('chef', 'chef@test.com', 'pass1234')
        self.cat = Category.objects.create(name='Indian', slug='indian')
        self.recipe = Recipe.objects.create(
            title='Dal', slug='dal', author=self.user, category=self.cat,
            description='Lentils', instructions='Cook',
            prep_time=10, cook_time=20, servings=4
        )

    def test_home(self):
        resp = self.client.get(reverse('recipes:home'))
        self.assertEqual(resp.status_code, 200)

    def test_recipe_list(self):
        resp = self.client.get(reverse('recipes:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Dal')

    def test_recipe_detail(self):
        resp = self.client.get(reverse('recipes:detail', args=['dal']))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Dal')

    def test_recipe_create_requires_login(self):
        resp = self.client.get(reverse('recipes:create'))
        self.assertEqual(resp.status_code, 302)

    def test_recipe_create_logged_in(self):
        self.client.login(username='chef', password='pass1234')
        resp = self.client.get(reverse('recipes:create'))
        self.assertEqual(resp.status_code, 200)

    def test_recipe_update_requires_author(self):
        other = User.objects.create_user('other', 'o@t.com', 'pass1234')
        self.client.login(username='other', password='pass1234')
        resp = self.client.get(reverse('recipes:update', args=['dal']))
        self.assertIn(resp.status_code, [302, 403, 404])

    def test_recipe_delete_requires_login(self):
        resp = self.client.get(reverse('recipes:delete', args=['dal']))
        self.assertEqual(resp.status_code, 302)

    def test_print_recipe(self):
        resp = self.client.get(reverse('recipes:print', args=['dal']))
        self.assertEqual(resp.status_code, 200)
