'''Unit test for SCache library.'''
import unittest

from flask import Flask
from http import HTTPStatus

from slib.log import SLog

from server.example.api import example
from server.error.handler import handler

class TestSErverExample(unittest.TestCase):
    '''Test case class.'''

    def setUp(self):
        '''Set up function.'''

        SLog.init()

        app = Flask(__name__)
        app.config['TESTING'] = True

        app.register_blueprint(handler)
        app.register_blueprint(example)

        self.cli = app.test_client()

    def tearDown(self):
        '''Tear down function.'''

    def test_root_path(self):
        '''Test / path.'''

        ret = self.cli.get('/')

        self.assertEqual(ret.status_code, HTTPStatus.OK)
        self.assertTrue('Hello to the world of Falsk!' in ret.data.decode('utf-8'))

    def test_show_key_path(self):
        '''Test show/<key> path.'''

        expected_message = 'example value of key message'

        test_key = 'message'

        ret = self.cli.get('/show/' + test_key)

        self.assertEqual(ret.status_code, HTTPStatus.OK)
        self.assertTrue(expected_message in ret.data.decode('utf-8'))

    def test_json_get_path(self):
        '''Test /json/get path.'''

        expected_json = '''{"arr1":["ele1","ele2","ele3"],''' \
            '''"dict1":{"dkey1":"dval1","dkey2":"dval2"},"key1":"val1","key2":"val2"}'''

        ret = self.cli.get('/json/get')

        self.assertEqual(ret.status_code, HTTPStatus.OK)
        self.assertTrue(expected_json in ret.data.decode('utf-8'))
