
""" pass """

from config import BaseTestClass
from config import api, load_time

class DouBanBooks(api.DouBanApi, BaseTestClass):
    """ pass """

    @classmethod
    def setUpClass(cls):
        """ pass """
        print(cls.enum)
        cls.schema_dir = 'douban'

    @load_time
    def test_get_douban_book_api(self):
        """ 这是 test_get_douban_book_api docstring """
        enum = self.get_value(self.enum, 'book_api_test')
        case_name = enum.get('name')
        test_api_url = enum.get('book_api')
        test_api_book_id = enum.get('book_id')
        resp = self.get(test_api_url.format(test_api_book_id)).json()
        self.assertEqual(self.valid_json(resp, self.schema_dir, case_name), True)

    @load_time
    def test_post_doiban_book_api(self):
        """ pass """
        enum = self.get_value(self.enum, 'search_book_api')
        case_name = enum.get('name')
        test_api_url = enum.get('search_api_url')
        keywords = "鲁滨逊漂流记"
        resp = self.get(test_api_url.format(keywords)).json()
        self.assertEqual(resp.get('count'), 20)
        self.assertEqual(self.valid_json(resp, self.schema_dir, case_name), True)
    
    @load_time
    def test_post_douban_book(self):
        """ pass """
        enum = self.get_value(self.enum, 'search_book_api')
        case_name = enum.get('name')
        test_api_url = enum.get('search_api_url')
        keywords = "三国演义"
        print(test_api_url.format(keywords))
        resp = self.get(test_api_url.format(keywords)).json()
        self.assertEqual(resp.get('count'), 20)
        self.assertEqual(self.valid_json(resp, self.schema_dir, case_name), True)
