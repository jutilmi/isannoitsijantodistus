"""This module consists of database connections procedures to
   various databases
"""

import sqlite3
import mysql.connector
import pyodbc

class Database():
    """This class has query connections to database"""

    def __init__(self, database, database_type, host='localhost', username=None, password=None):
        """This function initializes connection to server and database

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

    def connect_database(self):
        """Module creates a connection to a database and
           performs SQL query and closes the connection

           Keyword arguments:
           database                  -- str, path to database file or server
           database_type             -- str, ACCESS/SQLite/MySQL
           """

        if self.database_type == 'ACCESS':
            conn_str = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
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

    def query(self, sql_string):
        """Module creates connection, performs SQL query and closes the connection

           Keyword arguments:
           SQL_STRING                -- str, SQL query phrase

           Returns:
           SQL result                -- list
        """

        if self.cursor is None:
            try:
                self.cursor = self.conn.cursor()
            except ConnectionError:
                self.connect_database()
                self.cursor = self.conn.cursor()
        self.cursor.execute(sql_string)

        return self.cursor.fetchall()

    def close_connection(self):
        """This function closes database connection

           Keyword arguments:
           connection                -- pyodbc.connect or sqlite3.connect
        """

        if self.conn is not None:
            self.conn.close()
