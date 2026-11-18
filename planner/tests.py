from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from recipes.models import Recipe
from .models import MealPlan, MealPlanItem
from datetime import date, timedelta


class MealPlanModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('chef', 'c@t.com', 'pass1234')
        today = date.today()
        self.monday = today - timedelta(days=today.weekday())
        self.plan = MealPlan.objects.create(user=self.user, week_start=self.monday)

    def test_str(self):
        self.assertIn('chef', str(self.plan))

    def test_unique_together(self):
        with self.assertRaises(Exception):
            MealPlan.objects.create(user=self.user, week_start=self.monday)


class MealPlanItemTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('chef', 'c@t.com', 'pass1234')
        self.recipe = Recipe.objects.create(
            title='Dal', slug='dal', author=self.user,
            description='Lentils', instructions='Cook',
            prep_time=10, cook_time=20, servings=4
        )
        today = date.today()
        monday = today - timedelta(days=today.weekday())
        self.plan = MealPlan.objects.create(user=self.user, week_start=monday)

    def test_create_item(self):
        item = MealPlanItem.objects.create(
            meal_plan=self.plan, recipe=self.recipe, day=0, meal_type='breakfast'
        )
        self.assertIn('Monday', str(item))


class PlannerViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('chef', 'c@t.com', 'pass1234')
        self.recipe = Recipe.objects.create(
            title='Dal', slug='dal', author=self.user,
            description='Lentils', instructions='Cook',
            prep_time=10, cook_time=20, servings=4
        )

    def test_planner_requires_login(self):
        resp = self.client.get(reverse('planner:meal_planner'))
        self.assertEqual(resp.status_code, 302)

    def test_planner_logged_in(self):
        self.client.login(username='chef', password='pass1234')
        resp = self.client.get(reverse('planner:meal_planner'))
        self.assertEqual(resp.status_code, 200)

    def test_add_meal(self):
        self.client.login(username='chef', password='pass1234')
        resp = self.client.get(reverse('planner:add_meal', args=[0, 'breakfast', 'dal']))
        self.assertIn(resp.status_code, [200, 302])

    def test_shopping_list_requires_login(self):
        resp = self.client.get(reverse('planner:shopping_list'))
        self.assertEqual(resp.status_code, 302)

    def test_shopping_list_logged_in(self):
        self.client.login(username='chef', password='pass1234')
        resp = self.client.get(reverse('planner:shopping_list'))
        self.assertEqual(resp.status_code, 200)
