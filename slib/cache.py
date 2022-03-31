# pylint: disable=W0603
'''Redis memory cache library.'''
import redis
from slib.config import SConfig

SCACHE = None

class MemoryCacheHashKeyNotFound(Exception):
    '''Rised when hash key not found.'''

class MemoryCacheKeyNotFound(Exception):
    '''Rised when key not found.'''

class SCache():
    '''Access default memory cache.'''

    @staticmethod
    def init(host=None, port=None):
        '''Initialize memory cache.'''
        global SCACHE

        if host is not None:
            SCACHE = redis.StrictRedis(host, port, encoding="utf-8", decode_responses=True)
        else:
            host = SConfig.get_str_conf('memory_cache_host')
            port = SConfig.get_int_conf('memory_cache_port')
            SCACHE = redis.StrictRedis(host, port, encoding="utf-8", decode_responses=True)

    @staticmethod
    def hset(hashkey, key, value):
        '''set a hash value.'''

        return SCACHE.hset(hashkey, key, value)

    @staticmethod
    def hget(hashkey, key):
        '''get a specified value.'''

        ret_val = SCACHE.hget(hashkey, key)

        if ret_val is None:
            raise MemoryCacheKeyNotFound

        return ret_val

    @staticmethod
    def hdel(hashkey, key):
        '''delete a specified value.'''

        ret_val = SCACHE.hdel(hashkey, key)

        if ret_val == 0:
            raise MemoryCacheKeyNotFound

        return ret_val

    @staticmethod
    def hexists(hashkey, key):
        '''check whether the specified value exist.'''

        return SCACHE.hexists(hashkey, key)

    @staticmethod
    def hkeys(hashkey):
        '''get all keys in the specified hash.'''

        ret_val_list = SCACHE.hkeys(hashkey)

        if not ret_val_list:
            raise MemoryCacheHashKeyNotFound

        return ret_val_list
