from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class ToDoFunctionalTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_todo_app_functionalities(self):
        self.browser.get('http://localhost:8000')

        # Test tile, header text
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Test text field appearance
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Test _ToDo form
        inputbox.send_keys('Django guys, what to do now?')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Test the listed items
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn("Django guys, what to do now?", [row.text[3:] for row in rows])

