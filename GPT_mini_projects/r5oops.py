"""
Banking System (OOP Mini Project)

Concepts Used:
- Encapsulation (private variables, getters)
- Inheritance and method overriding
- Abstraction using abc module

Purpose:
Practice Object-Oriented Programming in Python.
"""


from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class BankAccount:
    def __init__(self, name, bal):
        self.name = name
        self.__balance = bal
    
    def deposit(self, amt):
        if(amt > 0):
            self.__balance += amt
            print(f"Deposit of {amt} successful\nBalance: {self.__balance}\n")
        else:
            print("Invalid amount\n")
    
    def withdraw(self, amt):
        if(amt <= self.__balance and amt > 0):
            self.__balance -= amt
            print(f"Withdrawal of {amt}rs successful\nBalance: {self.__balance}\n")
        else:
            print("Insufficient balance!\n")

    def get_balance(self):
        return self.__balance

    def is_high_val_acc(self):
        return self.__balance >= 2_00_000
 
    
class SavingsAccount(BankAccount):
    def __init__(self, name, bal, interest_rate):
        super().__init__(name, bal)
        self.interest_rate = interest_rate

    def increment(self):
        balance = self.get_balance()

        if(balance >= 50_000):
            amt_increased = balance * self.interest_rate / 100
            print(f"Increased balance by {self.interest_rate}%\nIncreased Amount: {amt_increased}\n")
            super().deposit(amt_increased)
        else:
            print("Balance should be greater than or equal to Rs50,000 to increase\n")

    def withdraw(self, amt):
        balance = self.get_balance()
        if(amt > 10_000):
            print("Cannot withdraw more than 10,000 per transaction!\n")
        else:
            super().withdraw(amt)


acc1 = SavingsAccount("Sony", 18_000, 5)
balance = acc1.get_balance()
acc1.deposit(3_000)
acc1.withdraw(1_000)
acc1.increment()
print(f"Is high value account: {acc1.is_high_val_acc()}\n")
acc1.deposit(50_000)
acc1.increment()
acc1.withdraw(1_000)
