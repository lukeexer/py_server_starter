'''Unit test for Web Server Example Module.'''
from operator import truediv
import unittest

from flask import Flask

from server.example.views import example

class TestServerExample(unittest.TestCase):
    '''Test case class.'''

    def setUp(self):
        '''Set up function.'''
        
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.env = 'development'

        # Register your server endpoint module here.
        app.register_blueprint(example)

        self.app = app.test_client()

    def tearDown(self):
        '''Tear down function.'''

    def test_hget(self):
        '''Test hget function.'''

        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)
