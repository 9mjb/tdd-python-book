#!/usr/bin/env python3

# ######################################################
# ######################################################
# ######################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # immediate invite to enter an item
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual( input_box.get_attribute('placeholder'),
                          'Enter a to-do item')

        # Enter text: "Buy peacock feathers"
        input_box.send_keys('peacock feathers')

        # <enter> that, and updated page has an item "Buy peacock feathers"
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        input_table = self.browser.find_element_by_id('id_list_table')
        rows = input_table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.txt == '1: Buy peacock feathers' for row in rows),
                        "New to-do item did not appear in table")

        self.fail('Finish the test!')
        # and it still has a new entry text box



        # Enter text: "Use feathers to make a fishing lure"
        # <enter> that, and updated page both items in the list
        # site generates, offers, and explains a custom link
        # visiting custom link shows the todo list


if __name__ == '__main__':
    unittest.main()  # warnings='ignore'
