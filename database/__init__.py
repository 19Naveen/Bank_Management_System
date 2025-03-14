import mysql.connector
from config.db_config import DB_CONFIG
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.cursor = None
        self.conn = None

    def create_connection(self):
        try:
            if not self.conn:
                self.conn = mysql.connector.connect(**DB_CONFIG)
                self.cursor = self.conn.cursor()
                print("Connected to the database!")
        except mysql.connector.Error as e:
            print(f"Database Connection Error: {e}")
            self.conn = None
            self.cursor = None

    def execute(self, query, values=()):
        '''NOTE: Execute a query and return the result if it is a SELECT query.'''
        if not self.conn:
            self.create_connection()

        try:
            self.cursor.execute(query, values)
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"❌ SQL Execution Error: {e}")

    def execute_fetchone(self, query, values=()):
        '''NOTE: Execute a query and return the result if it is a SELECT query.'''
        if not self.conn:
            self.create_connection()

        try:
            self.cursor.execute(query, values)
            if 'SELECT' in query:
                return self.cursor.fetchone()
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"❌ SQL Execution Error: {e}")


    def execute_fetchall(self, query, values=()):
        '''NOTE: Execute a query and return the result if it is a SELECT query.'''
        if not self.conn:
            self.create_connection()

        try:
            self.cursor.execute(query, values)
            if 'SELECT' in query:
                return self.cursor.fetchall()
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"❌ SQL Execution Error: {e}")

    def extract_last_id(self):
        '''NOTE: Extract the last inserted ID from the last executed query.'''
        return self.cursor.lastrowid

    def fetch_all(self):
        """Fetch all rows from the last executed query."""
        return self.cursor.fetchall() if self.cursor else None

    def fetch_one(self):
        """Fetch a single row from the last executed query."""
        return self.cursor.fetchone() if self.cursor else None

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("Connection closed!")

