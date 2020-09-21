#!/usr/bin/env python3

# ######################################################
# ######################################################
# ######################################################
from selenium import webdriver
import unittest # (ff https://docs.python.org/3/library/unittest.html)

class NewVisitorTest(unittest.TestCase):

    def setUp(self): # run before each test
        self.browser = webdriver.Chrome()

    def tearDown(self): # run after each test
        self.browser.quit()

    def test_can_start_a_list_and_retreive_it_later(self):
        """ test* functions are tests... """
        # check homepage
        self.browser.get('http://localhost:8000')

        # title
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # immediate invite to enter an item
        # Enter text: "Buy peacock feathers"
        # <enter> that, and updated page has an item "Buy peacock feathers"
        # and it still has a new entry text box
        # Enter text: "Use feathers to make a fishing lure"
        # <enter> that, and updated page both items in the list
        # site generates, offers, and explains a custom link
        # visiting custom link shows the todo list

if __name__ == '__main__':
    unittest.main()  # warnings='ignore'
