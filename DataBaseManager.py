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

    # Insert a transaction into the database
    def insert_transaction(self,amount,category,date,type,description = ""):
        self.cursor.execute("""
        INSERT INTO transactions (amount, category, date, type, description)
        VALUES (?, ?, ?, ?, ?)
        """, (amount,category,date,type,description))
        self.conn.commit()
    
    # Gets transaction
    def fetch_transaction(self,filter_by = None, value = None):
        if filter_by == 'category':
            self.cursor.execute("SELECT * FROM transactions WHERE category = ?", (value,))
        elif filter_by == 'date':
            self.cursor.execute("SELECT * FROM transactions WHERE date = ?", (value,))
        else:
            self.cursor.execute("SELECT * FROM transactions")
        return self.cursor.fetchall()

    # Delete a transaction by its ID
    def delete_transaction(self, transaction_id):
        self.cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
        self.conn.commit()


    # Calculates the balance (total income - total expense)
    def get_balance(self):
        self.cursor.execute("SELECT SUM(amount) FROM transactions WHERE type = 'income'")
        income = self.cursor.fetchone()[0] or 0 # default to 0 if None
        self.cursor.execute("SELECT SUM(amount) FROM transactions WHERE type = 'expense'")
        expense = self.cursor.fetchone()[0] or 0 # default to 0 if None
        return income - expense

    # Close the DB connection
    def close_connection(self):
        self.conn.close()

    # Run the script to create the database
if __name__ == "__main__":
    db = DatabaseManager()
    print("Database created successfully!")
    db.close_connection()