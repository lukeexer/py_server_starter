# pylint: disable=R0902
'''Unit test for SValidate library.'''
import unittest
import os

from slib.config import SConfig
from slib.config import ConfigNotFound
from slib.config import ConfigDataTypeNotMatch

class TestSConfig(unittest.TestCase):
    '''Test case class.'''

    def setUp(self):
        '''Set up function.'''

        self.config_file_name = 'test.conf'

        self.int_key_1 = 'int_val_1'
        self.str_key_1 = 'str_val_1'
        self.int_key_2 = 'int_val_2'
        self.str_key_2 = 'str_val_2'

        self.int_val_1 = 45
        self.str_val_1 = 'yes'
        self.int_val_2 = 9
        self.str_val_2 = 'no'

        with open(self.config_file_name, 'w', encoding='utf-8') as file:
            file.write('[CONFIG] ; Don\'t modify this section declaration!\n')
            file.write('\n')
            file.write('; configurations for testing.\n')
            file.write(f'{self.int_key_1} = {self.int_val_1}\n')
            file.write(f'{self.str_key_1} = {self.str_val_1}\n')
            file.write(f'{self.int_key_2} = {self.int_val_2}\n')
            file.write(f'{self.str_key_2} = {self.str_val_2}\n')

        SConfig.init(self.config_file_name)

    def tearDown(self):
        '''Tear down function.'''

        os.remove(self.config_file_name)

    def test_get_str_conf(self):
        '''Get a string value from configuration file.'''

        ret_val = SConfig.get_str_conf(self.str_key_1)

        self.assertEqual(self.str_val_1, ret_val)

    def test_get_str_conf_with_wrong_key(self):
        '''Get exception when key is not in configuration file.'''

        with self.assertRaises(ConfigNotFound):
            SConfig.get_str_conf('key_not_exist')

    def test_get_int_conf(self):
        '''Get a integer value from configuration file.'''

        ret_val = SConfig.get_int_conf(self.int_key_1)

        self.assertEqual(self.int_val_1, ret_val)

    def test_get_int_conf_type_not_match(self):
        '''Get a integer value from configuration file with wrong type.'''

        with self.assertRaises(ConfigDataTypeNotMatch):
            SConfig.get_int_conf(self.str_key_1)

    def test_get_int_conf_with_wrong_key(self):
        '''Get exception when key is not in configuration file.'''

        with self.assertRaises(ConfigNotFound):
            SConfig.get_int_conf('key_not_exist')

    def test_conf_exist(self):
        '''Check a specific key exists in configuration file.'''

        ret_val = SConfig.is_conf_exist(self.str_key_2)

        self.assertTrue(ret_val)

    def test_is_conf_not_exist(self):
        '''Check a specific key not exists in configuration file.'''

        ret_val = SConfig.is_conf_exist('key_not_exist')

        self.assertFalse(ret_val)

    def test_get_all_keys(self):
        '''Check all keys exist.'''

        keys = SConfig.get_all_keys()

        self.assertIn(self.int_key_1, keys)
        self.assertIn(self.str_key_1, keys)
        self.assertIn(self.int_key_2, keys)
        self.assertIn(self.str_key_2, keys)

    def test_get_all_key_and_value_pairs(self):
        '''Check all key and value pairs exist.'''

        key_val_pair = SConfig.get_all_key_and_value_pairs()

        self.assertIn((self.int_key_1, str(self.int_val_1)),  key_val_pair)
        self.assertIn((self.str_key_1, self.str_val_1), key_val_pair)
        self.assertIn((self.int_key_2, str(self.int_val_2)), key_val_pair)
        self.assertIn((self.str_key_2, self.str_val_2), key_val_pair)
