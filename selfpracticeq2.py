class Account:
    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance=balance
    def display(self):
        print(f"Account no:{self.acc_no}\nBalance:{self.balance}")

class SavingsAccount(Account):
    def __init__(self,acc_no,balance,interest):
        super().__init__(acc_no,balance)
        self.interest=interest
    def display(self):
        super().display()
        print(f"interest:{self.interest}")
a1=SavingsAccount(12321232,50000,12000)
a1.display()