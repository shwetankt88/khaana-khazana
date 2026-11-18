from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from recipes.models import Recipe
from .models import Review


class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('chef', 'c@t.com', 'pass1234')
        self.recipe = Recipe.objects.create(
            title='Dal', slug='dal', author=self.user,
            description='Lentils', instructions='Cook',
            prep_time=10, cook_time=20, servings=4
        )

    def test_create_review(self):
        r = Review.objects.create(recipe=self.recipe, user=self.user, rating=5, comment='Great!')
        self.assertIn('chef', str(r))
        self.assertIn('Dal', str(r))

    def test_unique_together(self):
        Review.objects.create(recipe=self.recipe, user=self.user, rating=4, comment='Nice')
        with self.assertRaises(Exception):
            Review.objects.create(recipe=self.recipe, user=self.user, rating=5, comment='Wow')


class ReviewViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('chef', 'c@t.com', 'pass1234')
        self.recipe = Recipe.objects.create(
            title='Dal', slug='dal', author=self.user,
            description='Lentils', instructions='Cook',
            prep_time=10, cook_time=20, servings=4
        )

    def test_add_review_requires_login(self):
        resp = self.client.post(reverse('reviews:add_review', args=['dal']), {
            'rating': 5, 'comment': 'Yummy'
        })
        self.assertEqual(resp.status_code, 302)

    def test_add_review_logged_in(self):
        self.client.login(username='chef', password='pass1234')
        resp = self.client.post(reverse('reviews:add_review', args=['dal']), {
            'rating': 5, 'comment': 'Yummy'
        })
        self.assertIn(resp.status_code, [200, 302])
        self.assertEqual(Review.objects.count(), 1)
