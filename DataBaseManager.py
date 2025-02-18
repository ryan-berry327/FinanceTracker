import sqlite3

class DatabaseManager:

    # Initialise the database connection
    def __init__(self, db_name = "finance.db"):
        self.conn = sqlite3.connect(db_name) #Can set up different db in the future if want to by removing the given db name
        self.cursor = self.conn.cursor()
        self.create_tables() # automatically create tables when the class is initialised


    def create_tables(self):
        # If table doesn't exist, create it
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,  -- ✅ FIXED MISSING COMMA
            date TEXT NOT NULL CHECK(date LIKE '____-__-__'),  -- Ensures YYYY-MM-DD format
            type TEXT CHECK(type IN ('income', 'expense')) NOT NULL,
            description TEXT DEFAULT '',
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        self.conn.commit()  # Save changes

    def insert_transaction(self,transaction):
        pass
    
    def fetch_transaction():
        pass

    def delete_transaction(transaction_id):
        pass

    def get_balance(self):
        pass
    # Close the DB connection
    def close_connection(self):
        self.conn.close()

    # Run the script to create the database
if __name__ == "__main__":
    db = DatabaseManager()
    print("Database created successfully!")
    db.close_connection()