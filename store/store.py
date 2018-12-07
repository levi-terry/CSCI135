class Transaction:
    def __init__(self, date, type, description, amount):
        self.date = date
        self.type = type
        self.description = description
        self.amount = amount

    def __str__(self):
        return "Date: " + self.date + ", Description: " + self.description + ", Amount: $" + self.amount


def print_number_of_transactions(list_of_trans):
    print("Number of transactions: %d" % len(list_of_trans))


def print_expenses(list_of_trans):
    expenses = []
    expenses_total = 0
    for transaction in list_of_trans:
        if transaction.type == "expense":
            expenses.append(transaction)
    print("Expenses: ")
    for expense in expenses:
        print(expense)
        expenses_total += int(expense.amount)
    print("Total Expenses: $%d.00" % expenses_total)


def print_deposits(list_of_trans):
    deposits = []
    deposits_total = 0
    for transaction in list_of_trans:
        if transaction.type == "deposit":
            deposits.append(transaction)
    print("Deposits:")
    for deposit in deposits:
        print(deposit)
        deposits_total += int(deposit.amount)
    print("Total Deposits: $%d.00" % deposits_total)


def print_balance(list_of_trans):
    account_balance = 0
    for transaction in list_of_trans:
        if transaction.type == "expense":
            account_balance -= int(transaction.amount)
        if transaction.type == "deposit":
            account_balance += int(transaction.amount)
    print("Balance: $%d.00" % account_balance)
    if account_balance < 0:
        print("In danger of going out of business!")


def generate_report(list_of_trans):
    pass


if __name__ == "__main__":
    list_of_transactions = []
    trans_file = open("transactions.txt")
    for line in trans_file:
        temp_line = line.split()
        transact = Transaction(temp_line[0], temp_line[1], temp_line[2], temp_line[3])
        list_of_transactions.append(transact)
        print(transact)
    trans_file.close()

    print("STORE")
    print("1. Print total number of transactions")
    print("2. Print expenses")
    print("3. Print deposits")
    print("4. Print account balance")
    print("5. Generate report")
    print("6. Quit")
