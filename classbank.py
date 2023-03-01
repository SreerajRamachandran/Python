class BankAccount:

    def __init__(self, account_number, name, account_type, balance=0):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def showamount(self):
        print("Account holder name:", self.name)
        print("Account number:", self.account_number)
        print("Account type:", self.account_type)
        print("Balance amount:", self.balance)

    def depo(self, d):
        self.balance = self.balance + d
        return self.balance

    def widrawal(self, w):
        self.balance = self.balance - w
        return self.balance


n = input("enter your name:")
a = int(input("enter the account number"))
t = input("enter the account type:")
o = BankAccount(a, n, t, balance=0)
o.showamount()
while (True):
    print("\nMenu")
    print("\n1.ddeposit")
    print("\n2.withdraw")
    c = int(input("enter your choice"))
    if (c == 1):
        d = int(input("enter the amount to deposit"))
        print("total balace", o.depo(d))
    elif (c == 2):
        w = int(input("enter the amount to withdraw"))
        if (w > d):
            print("insufficient balance")
        else:
            print("balnce is", o.widrawal(w))
    else:
        print("enter valid choice")
