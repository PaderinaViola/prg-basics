class Bank:
    def __init__(self, acc_no):
        self.balance = 0
        self.acc_no = acc_no

    def deposit(self, amount_deposit):
        self.balance += amount_deposit
        print(f"Successfully put {amount_deposit} PLN on the account!")

    def withdraw(self, amount_withdraw):
        if amount_withdraw <= self.balance:
            self.balance -= amount_withdraw
            print(f"Successfully withdrew {amount_withdraw} PLN!")
        else:
            print("Insufficient funds on the account")

    def display_status(self):
        print(f"Bank Account No: {self.acc_no}")
        print(f"Balance: PLN {self.balance}")
