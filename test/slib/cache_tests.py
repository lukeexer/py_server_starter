'''Unit test for SCache library.'''
import unittest

from slib.cache import SCache
from slib.cache import MemoryCacheKeyNotFound
from slib.cache import MemoryCacheHashKeyNotFound

class TestSCache(unittest.TestCase):
    '''Test case class.'''

    def setUp(self):
        '''Set up function.'''

        self.hash_name = 'test_hash'
        self.hash_key1 = 'key1'
        self.hash_value1 = 'value1'
        self.hash_key2 = 'key2'
        self.hash_value2 = 'value2'

        SCache.init('localhost', 6379)

        SCache.hset(self.hash_name, self.hash_key1, self.hash_value1)
        SCache.hset(self.hash_name, self.hash_key2, self.hash_value2)

    def tearDown(self):
        '''Tear down function.'''

        SCache.hdel(self.hash_name, self.hash_key1)
        SCache.hdel(self.hash_name, self.hash_key2)

    def test_hget(self):
        '''Test hget function.'''

        ret_val = SCache.hget(self.hash_name, self.hash_key1)

        self.assertEqual(self.hash_value1, ret_val)

    def test_hget_with_key_not_exist(self):
        '''Get exception when a specific key does not exist.'''

        with self.assertRaises(MemoryCacheKeyNotFound):
            SCache.hget(self.hash_name, 'Key_not_exist')

    def test_hdel_with_key_not_exist(self):
        '''Get exception when a specific key does not exist.'''

        with self.assertRaises(MemoryCacheKeyNotFound):
            SCache.hdel(self.hash_name, 'Key_not_exist')

    def test_hset(self):
        '''Test hset function.'''

        test_key = 'key3'
        test_value = 'value3'

        SCache.hset(self.hash_name, test_key, test_value)

        ret_val = SCache.hget(self.hash_name, test_key)

        self.assertEqual(test_value, ret_val)

    def test_hexists(self):
        '''Test hexists function.'''

        ret_val = SCache.hexists(self.hash_name, self.hash_key1)

        self.assertTrue(ret_val)

    def test_hkeys(self):
        '''Test hkeys function.'''

        ret_val = SCache.hkeys(self.hash_name)

        self.assertEqual(self.hash_key1, ret_val[1])
        self.assertEqual(self.hash_key2, ret_val[2])

    def test_hkeys_with_key_not_exist(self):
        '''Get exception when hash key does not exist.'''

        with self.assertRaises(MemoryCacheHashKeyNotFound):
            SCache.hkeys('hash_key_not_exist')
