import unittest
from selenium import webdriver


class FunctionalTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_it_returns_json_response_containing_image_urls_and_titles(self):
        # Josh wanted to use an image search api which can return a json
        # response containing image urls with alt text. Josh's friend refered
        # him to "this" api. 
        # Josh enters the url in browser address bar. 
        self.browser.get("http://localhost:8000/")

        # He saw an intro page containing an input box and instructions on api usage.
        input_tag = self.browser.find_element_by_class_name("search-input")

        self.assertEqual(input_tag.tag_name, "input")


if __name__ == "__main__":
    unittest.main()
