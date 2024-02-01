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
    
    #  string containing the balance: "The balance is X euros" 
    def __str__(self):
        return "The balance is {:.1f} euros".format(self.balance)
    
def main():
    card=LunchCard(6)
    print(card)
    card.eat_ordinarly()
    print(card)
    card.eat_luxuriously()
    card.eat_ordinarly()
    print(card)

if __name__ == "__main__":
    main()