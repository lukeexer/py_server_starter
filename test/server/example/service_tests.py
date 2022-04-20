'''Unit test for example service.'''
import unittest

from unittest.mock import MagicMock
from server.example.service import ExampleService
from server.example.repository import ExampleRepo

class TestExampleService(unittest.TestCase):
    '''Test case class.'''

    def setUp(self):
        '''Set up function.'''

        self.mock_repo = ExampleRepo()
        self.mock_repo.get_example_data = MagicMock(return_value='default message')

        self.service = ExampleService(self.mock_repo)

    def tearDown(self):
        '''Tear down function.'''

    def test_get_example_data(self):
        '''Test get_example_data function.'''

        default_key = 'default'
        expected_default_msg = 'default message'

        actual_default_msg = self.service.get_message(default_key)

        self.assertEqual(actual_default_msg, expected_default_msg)
