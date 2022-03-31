# pylint: disable=W0603
'''Sqlite library.'''

import sqlite3
from slib.config import SConfig

SQLITE_FILE = None

class MemoryCacheKeyNotFound(Exception):
    '''Rised when key not found.'''

class SSqlite():
    '''Access Sqlite database.'''

    @staticmethod
    def init(file=None):
        '''Initialize Sqlite database.'''

        global SQLITE_FILE

        if file is not None:
            SQLITE_FILE = file
        else:
            SQLITE_FILE = SConfig.get_str_conf('sqlite_db_file_name')

    @staticmethod
    def execute(sql=None):
        '''Execute SQL command.'''

        conn = sqlite3.connect(SQLITE_FILE)

        cur = conn.cursor()

        count = cur.execute(sql).rowcount

        conn.commit()

        conn.close()

        return count

    @staticmethod
    def fetch_all(sql=None):
        '''Fetch all query result from database.'''

        conn = sqlite3.connect(SQLITE_FILE)

        cur = conn.cursor()

        cur.execute(sql)

        result = cur.fetchall()

        conn.commit()

        conn.close()

        return result
