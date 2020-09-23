from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page  # (ff views.py)

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_home_html(self):
        #request = HttpRequest()
        #response = home_page(request)
        response = self.client.get('/')                # (ff ../functional_tests.py)
        self.assertTemplateUsed(response, 'home.html') # (ff templates/home.html)

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith( ('</html>','</html>\n') ))

        #expected_html = render_to_string( 'home.html')
        #self.assertEqual(html,expected_html)

    def test_can_save_a_post_request(self):
        response = self.client.post('/', data={'item_text': 'A new List item'})
        self.assertIn('A new List item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html') # (ff templates/home.html)



#class SmokeTest(TestCase):
#    def test_bad_math(self):
#        self.assertEqual(1+1, 3)
