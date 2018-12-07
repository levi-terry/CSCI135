class Transaction:
    def __init__(self, date, type, description, amount):
        self.date = date
        self.type = type
        self.description = description
        self.amount = amount

    def __str__(self):
        return "Date:", self.date, "Description:", self.description, "Amount: $", self.amount


if __name__ == "__main__":
    def print_number_of_transactions(list_of_trans):
        # Prints number of transactions
        # "Number of transactions: X"
        pass

    def print_expenses(list_of_trans):
        # Prints the list of transactions that are expenses
        # "Expenses:\nTransaction"
        pass

    def print_deposits(list_of_trans):
        # Prints the list of transactions that are deposits
        # Just like above
        pass

    def print_balance(list_of_trans):
        pass

    def generate_report(list_of_trans):
        pass

    print("STORE")
    print("1. Print total number of transactions")
    print("2. Print expenses")
    print("3. Print deposits")
    print("4. Print account balance")
    print("5. Generate report")
    print("6. Quit")
