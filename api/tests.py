from django.core.urlresolvers import resolve
from django.test import TestCase

from .views import homepage


class HomepageTest(TestCase):

    def test_root_url_resolves_to_homepage(self):
        found = resolve("/")
        self.assertEqual(found.func, homepage)

    def test_homepage_renders_correct_template(self):
        res = self.client.get("/")

        self.assertTemplateUsed(res, "api/index.html")

