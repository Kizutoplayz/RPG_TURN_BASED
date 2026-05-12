import random as ra, math as ma, sys, os 

#Stats for player and enemies
class Stats:
    def __init__(self, attack, health, defense):               
        self.attack = attack
        self.health = health
        self.defense = defense

class Player(Stats):
    pass
class Enemy(Stats):
    pass

#misc
player = Player(5, 15, 2)
in_combat = False

#main game loop
def game_loop():
    global in_combat
    while(True):
        if not in_combat:
            c = input("Press [E] to explore. \n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if c == "E" or c == "e":
                print("You explore...\n")
                encount = ra.randint(1,5)
                if encount == 1:
                    in_combat = True
                    enemy = Enemy(ra.randint(1,5), ra.randint(10,20), ra.randint(0,3))
                else:
                    in_combat = False
            else:
                print("Put the correct terms.")
        
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Enemy Health: {enemy.health}")
            print(f"Player Health: {player.health}")
            c = input("\nPress [A] for Attack or [D] for Defend.\n")          #turns
            if c == "A" or c == "a":
                print("You attacked!")
                enemy.health -= ma.ceil(player.attack * (1 - enemy.defense / 100)) 
                print("Enemy attacked you back!\n")
                player.health -= ma.ceil(enemy.attack * (1 - player.defense / 100))
                if player.health <= 0:
                    print("You died!")
                    sys.exit()
                if enemy.health <= 0:
                    print("You killed the enemy.")
                    in_combat = False
            elif c == "D" or c == "d":
                print("You Defended.")
                player.health -= ma.ceil(enemy.attack * (1 - player.defense / 100))
                if player.health <= 0:
                    print("You died!")
                    sys.exit()
            else:
                print("\nPlease Put in the correct terms.\n")



if __name__ == "__main__":
    game_loop()