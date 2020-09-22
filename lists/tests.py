from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_reutrns_correct_html(self):
        request = HttpRequest()
        responce = home_page(request)
        html = responce.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

#class SmokeTest(TestCase):
#    def test_bad_math(self):
#        self.assertEqual(1+1, 3)
