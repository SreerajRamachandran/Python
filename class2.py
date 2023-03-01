##Create a Bank account with members account number, name, type of account and balance.
# Write constructor and methods to deposit at the bank and withdraw an amount from the bank

class Bank:
    def __init__(self, acno, name, type, balance=0):
        self.acno = acno
        self.name = name
        self.type = type
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"unsuccessfull insufficient fund")
        else:
            self.balance -= amount
            print(f"successfull ")

    def display(self):
        print(f"account number {self.acno}")
        print(f"name{self.name}")
        print(f"type {self.type}")
        print(f"balance {self.balance}")


member1 = Bank(123, "sree", "savings", 10000)
member1.deposit(2000)
member1.withdraw(5000)
member1.display()
