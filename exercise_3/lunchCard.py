# File: lunchCard.py
# Author: Kirill Nikolaev
# Description: emulating use of debit card

class LunchCard:
    def __init__(self, balance:float):
        self.balance =balance

    def eat_ordinarly(self):
        if self.balance - 2.95 < 0:
            print("Insufficient balance for ordinary lunch.")
        else:
            self.balance -= 2.95
    
    def eat_luxuriously(self):
        if self.balance - 5.90 < 0:
            print("Insufficient balance for luxurious lunch.")
        else:
            self.balance -= 5.90

    def deposit_money(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount.")
        self.balance += amount
    
    #  string containing the balance: "The balance is X euros" 
    def __str__(self):
        return "The balance is {:.1f} euros".format(self.balance)
    
def main():
    peter_card = LunchCard(20)
    grace_card = LunchCard(30)

    peter_card.eat_luxuriously()
    grace_card.eat_ordinarly()

    print("Peter: " + str(peter_card))
    print("Grace: " + str(grace_card))

    peter_card.deposit_money(20)
    grace_card.eat_luxuriously()

    print("Peter: " + str(peter_card))
    print("Grace: " + str(grace_card))

    peter_card.eat_ordinarly()
    peter_card.eat_ordinarly()
    grace_card.deposit_money(50)

    print("Peter: " + str(peter_card))
    print("Grace: " + str(grace_card))

if __name__ == "__main__":
    main()

