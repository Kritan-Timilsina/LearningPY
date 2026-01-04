class BankAccount:
  def __init__(self,__account_no,__balance):
   self.__account_no=__account_no
   self.__balance=__balance

  def deposit(self,amount):
   self.__balance=self.__balance+amount

  def withdraw(self,amount):
   self.__balance=self.__balance-amount

  def display(self):
   print(f"Account no:{self.__account_no}\nBalance:{self.__balance}")

p1=BankAccount(101,10001)
p1.display()
p1.deposit(100)
p1.display()
p1.withdraw(100)
p1.display()
