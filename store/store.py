import sys


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


def ret_num_trans(list_of_trans):
    return "Number of transactions: %d" % len(list_of_trans)


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


def ret_expenses(list_of_trans):
    expenses = []
    for transaction in list_of_trans:
        if transaction.type == "expense":
            expenses.append(transaction)
    return expenses


def total_expenses(list_of_trans):
    expenses = []
    expenses_total = 0
    for transaction in list_of_trans:
        if transaction.type == "expense":
            expenses.append(transaction)
    for expense in expenses:
        expenses_total += int(expense.amount)
    return expenses_total


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


def ret_deposits(list_of_trans):
    deposits = []
    for transaction in list_of_trans:
        if transaction.type == "deposit":
            deposits.append(transaction)
    return deposits


def total_deposits(list_of_trans):
    deposits = []
    deposits_total = 0
    for transaction in list_of_trans:
        if transaction.type == "deposit":
            deposits.append(transaction)
    for deposit in deposits:
        deposits_total += int(deposit.amount)
    return deposits_total


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


def ret_balance(list_of_trans):
    account_balance = 0
    for transaction in list_of_trans:
        if transaction.type == "expense":
            account_balance -= int(transaction.amount)
        if transaction.type == "deposit":
            account_balance += int(transaction.amount)
    return account_balance


def generate_report(list_of_trans):
    with open("report.txt", 'w') as report:
        report.write("STORE\n\n")
        report.write(ret_num_trans(list_of_trans))
        report.write("\n\nExpenses:\n\n")
        expenses = ret_expenses(list_of_trans)
        for expense in expenses:
            report.write(str(expense))
            report.write("\n")
        report.write("Total expenses: $")
        report.write(str(total_expenses(list_of_trans)))
        report.write("\n\n")
        report.write("Deposits:\n")
        deposits = ret_deposits(list_of_trans)
        for deposit in deposits:
            report.write(str(deposit))
            report.write("\n")
        report.write("Total deposits: $")
        report.write(str(total_deposits(list_of_trans)))
        report.write("\n\n")
        report.write("Balance: $")
        report.write(str(ret_balance(list_of_trans)))
        if ret_balance(list_of_trans) < 0:
            report.write("\nIn danger of going out of business!")


if __name__ == "__main__":
    list_of_transactions = []
    trans_file = open("transactions.txt")
    for line in trans_file:
        temp_line = line.split()
        transact = Transaction(temp_line[0], temp_line[1], temp_line[2], temp_line[3])
        list_of_transactions.append(transact)
    trans_file.close()

    generate_report(list_of_transactions)
    print("STORE")
    print("1. Print total number of transactions")
    print("2. Print expenses")
    print("3. Print deposits")
    print("4. Print account balance")
    print("5. Generate report")
    print("6. Quit")
    user_choice = input("Enter choice(1/2/3/4/5/6):")
    correct_choices = ["1", "2", "3", "4", "5", "6"]
    while user_choice not in correct_choices:
        print("Invalid input")
        print("STORE")
        print("1. Print total number of transactions")
        print("2. Print expenses")
        print("3. Print deposits")
        print("4. Print account balance")
        print("5. Generate report")
        print("6. Quit")
        user_choice = input("Enter choice(1/2/3/4/5/6):")
    if user_choice == "1":
        print_number_of_transactions(list_of_transactions)
    if user_choice == "2":
        print_expenses(list_of_transactions)
    if user_choice == "3":
        print_deposits(list_of_transactions)
    if user_choice == "4":
        print_balance(list_of_transactions)
    if user_choice == "5":
        generate_report(list_of_transactions)
    if user_choice == "6":
        exit()
