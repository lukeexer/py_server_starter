'''Unit test for SCache library.'''
import unittest

from flask import Flask

from slib.log import SLog

from server.example.api import example
from server.error.handler import handler

class TestSErverExample(unittest.TestCase):
    '''Test case class.'''

    def setUp(self):
        '''Set up function.'''

    def tearDown(self):
        '''Tear down function.'''

    def test_root_path(self):
        '''Test hget function.'''

        SLog.init()

        app = Flask(__name__)
        app.config['TESTING'] = True

        app.register_blueprint(handler)
        app.register_blueprint(example)

        cli = app.test_client()

        ret = cli.get('/')

        self.assertEqual(ret.status_code, 200)
        self.assertTrue('Hello to the world of Falsk!' in ret.data.decode('utf-8'))
