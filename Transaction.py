class Transaction:
    amount = 0
    category = ''
    date = ''
    type = '' # Either "income" or "expense"

    # If the transaction is an + it is income, if it is - it is an expense
    def display():
        if type.lower() == 'income':
            print(f"Income: /n Amount: {amount}Date: {date}, Category: {category}")
        elif type.lower() == 'expnese':
            print(f"Expense: /n Amount: {amount}Date: {date}, Category:{category}")
        else:
            print("Invalid transaction type")

    def to_dict():
        pass
