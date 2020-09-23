#!/usr/bin/env python3

# (ff lists/tests.py)
# (ff lists/templates/home.html)

# ######################################################
# ######################################################
# ######################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest # (ff https://docs.python.org/3/library/unittest.html)

class NewVisitorTest(unittest.TestCase):

    # #######################################################
    def setUp(self): # run before each test
        self.browser = webdriver.Chrome()

    def tearDown(self): # run after each test
        self.browser.quit()

    # #######################################################
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    # #######################################################
    def test_can_start_a_list_and_retreive_it_later(self):
        # """ test* functions are tests... """
        # check homepage
        self.browser.get('http://localhost:8000')

        # title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # immediate invite to enter an item
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual( input_box.get_attribute('placeholder'), 'Enter a to-do item')
        # Enter text: "Buy peacock feathers"
        input_box.send_keys('Buy peacock feathers')
        # <enter> that, and updated page has an item "Buy peacock feathers"
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        #
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        #self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows),
        #                f"New to-do item did not appear in table. Content was:\n{table.text}")
        # self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # Enter text: "Use feathers to make a fishing lure"
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual( input_box.get_attribute('placeholder'), 'Enter a to-do item')
        input_box.send_keys('Use pf to make a fly')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        # <enter> that, and updated page has both items in the list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use pf to make a fly')

        self.fail('Finish the test!')
        # and it still has a new entry text box



        # site generates, offers, and explains a custom link
        # visiting custom link shows the todo list


if __name__ == '__main__':
    unittest.main()  # warnings='ignore'
