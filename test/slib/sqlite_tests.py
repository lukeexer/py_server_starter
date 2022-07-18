'''
Unit test for Sqlite library.
Please refer to following link for data types.
https://www.sqlite.org/datatype3.html
'''
import unittest
import os

from slib.sqlite import SSqlite

class TestSSqlite(unittest.TestCase):
    '''Test case class.'''

    def setUp(self):
        '''Set up function.'''

        SSqlite.init('test.db')
        SSqlite.execute('''CREATE TABLE test_table \
            (test_date TEXT, test_text TEXT, test_int INTEGER, test_real REAL)''')
        SSqlite.execute('''INSERT INTO test_table \
            VALUES ('2006-01-05 12:20:30', 'text 1', 100, 3.14)''')
        SSqlite.execute('''INSERT INTO test_table \
            VALUES ('2007-02-05 13:20:30', 'text 2', 200, 3.16)''')
        SSqlite.execute('''INSERT INTO test_table \
            VALUES ('2008-03-05 14:20:30', 'text 3', 300, 3.18)''')

    def tearDown(self):
        '''Tear down function.'''

        SSqlite.execute('''DROP TABLE test_table''')

        os.remove('test.db')

    def test_execute(self):
        '''Test execute function.'''

        sql = '''INSERT INTO test_table VALUES ('2009-04-06 15:21:32', 'text 4', 400, 4.26)'''
        result = SSqlite.execute(sql)

        self.assertEqual(1, result)

    def test_fetch_all(self):
        '''Test fetch_all function.'''

        sql = '''SELECT * FROM test_table'''
        result = SSqlite.fetch_all(sql)

        self.assertEqual(3, len(result))

    def test_fetch_one(self):
        '''Test fetch_one function.'''

        sql = '''SELECT * FROM test_table WHERE test_int = 100;'''
        result = SSqlite.fetch_one(sql)

        self.assertEqual(4, len(result))
        self.assertTrue(str('text 1') in result[1])

    def test_lazy_execution(self):
        '''Test lazy execution function sets.'''

        (conn, cur) = SSqlite.lazy_connect()

        sql = '''INSERT INTO test_table VALUES ('2009-04-06 15:21:32', 'text 4', 400, 4.26)'''

        SSqlite.lazy_execute(cur, sql)

        SSqlite.lazy_commit(conn)

        sql = '''SELECT * FROM test_table'''
        result = SSqlite.fetch_all(sql)

        self.assertEqual(4, len(result))
