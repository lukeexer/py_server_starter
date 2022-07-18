'''Unit test for SCache library.'''
from unittest.mock import MagicMock, patch

import unittest
import redis

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

    def test_hget(self):
        '''Test hget function.'''

        mock_cache = redis.StrictRedis()
        mock_cache.hget = MagicMock(return_value=self.hash_value1)
        mock_cache.hget(self.hash_name, self.hash_key1)

        SCache.init(mock_cache)

        ret_val = SCache.hget(self.hash_name, self.hash_key1)

        self.assertEqual(self.hash_value1, ret_val)

    def test_hget_with_key_not_exist(self):
        '''Get exception when a specific key does not exist.'''

        mock_cache = redis.StrictRedis()
        mock_cache.hget = MagicMock(return_value=None)
        mock_cache.hget(self.hash_name, self.hash_key1)

        SCache.init(mock_cache)

        with self.assertRaises(MemoryCacheKeyNotFound):
            SCache.hget(self.hash_name, 'Key_not_exist')

    def test_hdel(self):
        '''Test hdel function.'''

        expectd_ret_val = 1

        mock_cache = redis.StrictRedis()
        mock_cache.hdel = MagicMock(return_value=1)
        mock_cache.hdel(self.hash_name, self.hash_key1)

        SCache.init(mock_cache)

        ret_val = SCache.hdel(self.hash_name, self.hash_key1)

        self.assertEqual(expectd_ret_val, ret_val)

    def test_hdel_with_key_not_exist(self):
        '''Get exception when a specific key does not exist.'''

        mock_cache = redis.StrictRedis()
        mock_cache.hdel = MagicMock(return_value=0)
        mock_cache.hdel(self.hash_name, 'Key_not_exist')

        SCache.init(mock_cache)

        with self.assertRaises(MemoryCacheKeyNotFound):
            SCache.hdel(self.hash_name, 'Key_not_exist')

    def test_hset(self):
        '''Test hset function.'''

        with patch.object(redis.StrictRedis, 'hset', return_value=1) as mock_cache_hset:
            mock_cache = redis.StrictRedis()

            SCache.init(mock_cache)

            SCache.hset(self.hash_name, self.hash_key1, self.hash_value1)

        mock_cache_hset.assert_called_once_with(self.hash_name, self.hash_key1, self.hash_value1)

    def test_hexists(self):
        '''Test hexists function with a existing key.'''

        expected_ret_val = True

        with patch.object(redis.StrictRedis, 'hexists', return_value=1) as mock_cache_hexists:
            mock_cache = redis.StrictRedis()

            SCache.init(mock_cache)

            actual_ret_val = SCache.hexists(self.hash_name, self.hash_key1)

        mock_cache_hexists.assert_called_once_with(self.hash_name, self.hash_key1)

        self.assertEqual(expected_ret_val, actual_ret_val)

    def test_hexists_with_not_existing_key(self):
        '''Test hexists function with a not existing key.'''

        expected_ret_val = False

        with patch.object(redis.StrictRedis, 'hexists', return_value=0) as mock_cache_hexists:
            mock_cache = redis.StrictRedis()

            SCache.init(mock_cache)

            actual_ret_val = SCache.hexists(self.hash_name, self.hash_key1)

        mock_cache_hexists.assert_called_once_with(self.hash_name, self.hash_key1)

        self.assertEqual(expected_ret_val, actual_ret_val)

    def test_hkeys(self):
        '''Test hkeys function.'''

        mock_cache = redis.StrictRedis()
        mock_cache.hkeys = MagicMock(return_value=[self.hash_key1, self.hash_key2])
        mock_cache.hkeys(self.hash_name)

        SCache.init(mock_cache)

        ret_val = SCache.hkeys(self.hash_name)

        self.assertEqual(self.hash_key1, ret_val[0])
        self.assertEqual(self.hash_key2, ret_val[1])

    def test_hkeys_with_key_not_exist(self):
        '''Get exception when hash key does not exist.'''

        mock_cache = redis.StrictRedis()
        mock_cache.hkeys = MagicMock(return_value=None)
        mock_cache.hkeys(self.hash_name, 'Key_not_exist')

        SCache.init(mock_cache)

        with self.assertRaises(MemoryCacheHashKeyNotFound):
            SCache.hkeys('Key_not_exist')
