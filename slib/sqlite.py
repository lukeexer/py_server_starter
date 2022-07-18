# pylint: disable=W0603
'''Sqlite library.'''

import sqlite3
from slib.config import SConfig

SQLITE_FILE = None

class MemoryCacheKeyNotFound(Exception):
    '''Raised when key not found.'''

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

    @staticmethod
    def fetch_one(sql=None):
        '''Fetch one query result from database.'''

        conn = sqlite3.connect(SQLITE_FILE)

        cur = conn.cursor()

        cur.execute(sql)

        result = cur.fetchone()

        conn.commit()

        conn.close()

        return result

    @staticmethod
    def lazy_connect():
        '''Get SQLite cursor.'''

        conn = sqlite3.connect(SQLITE_FILE)

        cur = conn.cursor()

        return (conn, cur)

    @staticmethod
    def lazy_execute(cur, sql):
        '''Execute SQL with cursor.'''

        cur.execute(sql)

    @staticmethod
    def lazy_commit(conn):
        '''Commit SQL commands.'''

        conn.commit()

        conn.close()
