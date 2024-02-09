# File: serviceCharge.py
# Author: Kirill Nikolaev
# Description: a class named BankAccount which models a bank account

class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float):
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount: float):
        if amount <= self.__balance:
            self.__balance -= amount
            self.__service_charge()

    @property
    def balance(self) -> float:
        return self.__balance

    def __service_charge(self):
        self.__balance -= self.__balance * 0.01

def main():
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)

if __name__ == "__main__":
    main()