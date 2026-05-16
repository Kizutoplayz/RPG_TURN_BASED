from Stat import Player
from random import randint
from Gamble import Gamble

class DiceRoll(Gamble):
    def __init__(self, player):
        super().__init__(player)

    def CheckBalance(self, wager):
        if wager < self.player.coin:
            return True
        else:
            return False
        
    def verdict(self, total, wager):
        if total == 7:
            return (wager * 5)
        if total == 6 or total == 8:
            return (wager * 2)
        if total == 5 or total == 9:
            return (wager * 1.5)
        if total == 4 or total == 10:
            return (wager)
        if total == 3 or total == 11:
            return (-wager)
        if total == 2 or total == 12:
            return (-wager)
    

    def dice_roll(self, wager):
        if self.CheckBalance(wager):

            self.player.coin -= wager

            dice1 = randint(1,6)
            dice2 = randint(1,6)
            total = dice1 + dice2

            result = self.verdict(total, wager)
            self.player.coin += result

            print("-------Dice Roll-------")
            print(f"Dice 1: {dice1}")
            print(f"Dice 2: {dice2}")
            if total >= 5 and total <= 9:
                print(f"You won {result} coins.")
            elif total == 4 or total == 10:
                print(f"You broke even. Your bet is returned")
            else:
                print(f"You lost {result} coins.")

        else:
            print("Not Enough Balance")

# Testing
#def main():
#    P = Player("Bezz",0,0,0, coin= 200)
#    A = DiceRoll(P) 
#    A.dice_roll(10)
#
#if __name__ == "__main__":
#    main()
        

            

        