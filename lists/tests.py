# tests.py
# mjb 2020/09/22

from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page  # (ff views.py)

# (ff https://docs.DjangoProject.com/en/1.11/intro/tutorial01/)
from lists.models import Item # (ff models.py)

# #######################################################
class ItemModelTest(TestCase):

    def test_saving_and_retreiving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item The second'
        second_item.save()
        
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item The second')

# #######################################################
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



# #######################################################
#class SmokeTest(TestCase):
#    def test_bad_math(self):
#        self.assertEqual(1+1, 3)

