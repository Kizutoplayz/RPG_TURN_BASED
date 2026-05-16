from Stat import Player
from random import randint
from Gamble import Gamble

class CoinFlip(Gamble):
    def __init__(self, player):
        super().__init__(player)

    def CheckBalance(self, wager):
        if wager < self.player.coin:
            return True
        else:
            return False


    def coin_flip(self, choice, wager):  

        if self.CheckBalance(wager):
            self.player.coin -= wager

            result = "h" if randint(0, 1) == 0 else "t"

            if result == choice:
                self.player.coin += wager * 2
                print(f"It was {"Heads" if result == "h" else "Tails"}.")
                print(f"You won {wager * 2} coins. Balance: {self.player.coin}")
            else:
                print(f"It was {"Tails" if result == "t" else "Heads"}.")
                print(f"You lost {wager} coins. Balance: {self.player.coin}")
        else:
             print("Not Enough Balance")



# Testing
#def main():
#    P = Player("Bezz",0,0,0, coin= 200)
#    A = CoinFlip(P) 
#    A.coin_flip("h", 100)
#
#if __name__ == "__main__":
#    main()