"""This module includes database class and its methods and other
   database related funcions for various database types.
   """
import sqlite3
import mysql.connector
import pyodbc

class SQL():
    """This class is for database initialization and queries."""

    def __init__(self, database: str, database_type: str,
                 host='localhost', username=None, password=None):
        """This function initializes connection to server and database.

           After initializing, connection to database is created with Database.connect(), and
           queried with Database.query(sql_string, *args). Output for query is fetch all. Close
           connection to database with Database.close().

           Keyword arguments:
           database                -- str, name of the database
           database_type           -- str, ACCESS/SQLite/MySQL
           host                    -- str, database host, default = localhost
           username                -- str, username to access host/database
           password                -- str, password to access host/database
           """

        self.database = database
        self.database_type = database_type
        self.host = host
        self.username = username
        self.password = password
        self.conn = None
        self.cursor = None

    def connect(self):
        """Method creates a connection to a database according to initialized parameters."""

        if self.database_type == 'ACCESS':
            conn_str = (
                r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=' + self.database + ';'
                )
            self.conn = pyodbc.connect(conn_str)
        elif self.database_type == 'SQLite':
            self.conn = sqlite3.connect(self.database)
        elif self.database_type == 'MySQL':
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.username,
                passwd=self.password,
                database=self.database
                )

    def query(self, sql_string: str, *args):
        """Method executes sql query.

           Keyword arguments:
           SQL_STRING                -- str, SQL query phrase
           args                      -- tuple, arguments for SQL query

           Returns:
           SQL result                -- list
           """

        if self.cursor is None:
            try:
                self.cursor = self.conn.cursor()
            except ConnectionError:
                self.connect()
                self.cursor = self.conn.cursor()
        self.cursor.execute(sql_string, *args)

        return self.cursor.fetchall()

    def close(self):
        """This function closes database connection."""

        if self.conn is not None:
            self.conn.close()
