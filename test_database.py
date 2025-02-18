from DatabaseManager import DatabaseManager

# Initialize the DatabaseManager
db = DatabaseManager()

# Insert some test transactions
db.insert_transaction(100.00, "Food", "2025-02-18", "expense", "Lunch")
db.insert_transaction(500.00, "Salary", "2025-02-18", "income", "Salary")
db.insert_transaction(50.00, "Food", "2025-02-19", "expense", "Snack")

# Test fetching all transactions
print("All Transactions:", db.fetch_transaction())

# Test fetching transactions by category
print("Food Transactions:", db.fetch_transaction('category', "Food"))

# Test fetching transactions by date
print("Transactions on 2025-02-18:", db.fetch_transaction('date', "2025-02-18"))

# Test getting balance
print("Current Balance:", db.get_balance())

# Test deleting a transaction
db.delete_transaction(1)  # Example: delete transaction with ID 1

# Test fetching after deletion
print("All Transactions After Deletion:", db.fetch_transaction())

# Close the database connection
db.close_connection()
