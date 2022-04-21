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

    def test_resource_not_found(self):
        '''Test resource not found.'''

        expected_ret_val = '''{"code":"S00003","msg":"resource not found"}'''

        ret = self.cli.get('/path_not_exist')

        self.assertEqual(ret.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
        self.assertTrue(expected_ret_val in ret.data.decode('utf-8'))

    def test_method_not_allowed(self):
        '''Test method not allowed.'''

        expected_ret_val = '''{"code":"S00002","msg":"method not allowed"}'''

        ret = self.cli.get('/post/example')

        self.assertEqual(ret.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
        self.assertTrue(expected_ret_val in ret.data.decode('utf-8'))

    def test_internal_server_error(self):
        '''Test internal server error.'''

        expected_ret_val = '''{"code":"S00004","msg":"internal server error"}'''

        ret = self.cli.get('/error/server')

        self.assertEqual(ret.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
        self.assertTrue(expected_ret_val in ret.data.decode('utf-8'))

    def test_unknown_runtime_exception(self):
        '''Test unknown runtime exception capture.'''

        expected_ret_val = '''{"code":"S00001","msg":"unknown error"}'''

        ret = self.cli.get('/error/exception')

        self.assertEqual(ret.status_code, HTTPStatus.INSUFFICIENT_STORAGE)
        self.assertTrue(expected_ret_val in ret.data.decode('utf-8'))
