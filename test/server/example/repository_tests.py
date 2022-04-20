'''Unit test for example repository.'''
import unittest

from server.example.repository import ExampleRepo

class TestExampleRepository(unittest.TestCase):
    '''Test case class.'''

    def setUp(self):
        '''Set up function.'''

        self.repo = ExampleRepo()

    def tearDown(self):
        '''Tear down function.'''

    def test_get_example_data(self):
        '''Test get_example_data function.'''

        default_key = 'default'
        expected_default_msg = 'default message'

        actual_default_msg = self.repo.get_example_data(default_key)

        self.assertEqual(actual_default_msg, expected_default_msg)

        message_key = 'message'
        expected_message_msg = 'example value of key message'

        actual_message_msg = self.repo.get_example_data(message_key)

        self.assertEqual(actual_message_msg, expected_message_msg)
