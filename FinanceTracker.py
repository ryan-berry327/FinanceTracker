class FinanceTracker:

    transactions = []
    database = '' # connect to sql database

    def add_transaction(transaction):
        transactions.append(transaction)

    def remove_transaction(transaction_id):
        for i, transaction in enumerate(transactions):
            if transaction == transaction_id:
                del transaction
        return transactions

    def get_transactions(filter_criteria):
        pass
    
    def calculate_balance():
        pass
    
    def generate_report():
        pass
