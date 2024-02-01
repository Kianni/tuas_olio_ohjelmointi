# File: lunchCard.py
# Author: Kirill Nikolaev
# Description: emulating use of debit card

class LunchCard:
    def __init__(self, balance:float):
        self.balance =balance
    
    #  string containing the balance: "The balance is X euros". 
    # The available balance should be printed out with one decimal place precision. 
    def __str__(self):
        return "The balance is {:.1f} euros".format(self.balance)
    
def main():
    card = LunchCard(50.0)
    print(card)

if __name__ == "__main__":
    main()