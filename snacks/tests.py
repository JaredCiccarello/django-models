from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from snacks.models import Snack


# Create your tests here.
# Run with
# python3 manage.py test

class SnackTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass")
        self.snack = Snack.objects.create(
            name='snack1', rating=10, reviewer=self.user)

    def test_string_representation(self):
        self.assertEqual(str(self.snack), 'snack1')

    def test_snack_name(self):
        self.assertEqual(f'{self.snack.name}', 'snack1')

    def test_list_page_status_code(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "base.html")

    def test_hard_coded_path(self):
        url = reverse("snack_list")
        self.assertEqual(url, "/")