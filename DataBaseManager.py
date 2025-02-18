import sqlite3

class DatabaseManager:

    # Initialise the database connection
    def __init__(self, db_name = "FinanceTracker.db"):
        self.conn = sqlite3.connect(db_name) #Can set up different db in the future if want to by removing the given db name
        self.cursor = self.conn.cursor()
        self.create_tables() # automatically create tables when the class is initialised


    def create_tables(self):

        # If table doesnt exist create it
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL
            category TEXT NOT NULL,
            date TEXT NOT NULL CHECK(date LIKE '____-__-__'), # Ensures YYYY-MM-DD format
            type TEXT CHECK(type IN ('income','expense')) NOT NULL,
            description TEXT DEFAULT '',
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.conn.commit() # save changes

    # Close the DB connection
    def close_connection(self):
        self.conn.close()

    def initialise_database():
        pass
    
    def insert_transaction(transaction):
        pass
    
    def fetch_transaction():
        pass

    def delete_transaction(transaction_id):
        pass

    