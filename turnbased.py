import random as ra, math as ma, sys, os 
from Stat import Player, Enemy

#Misc
in_combat = False
player = Player(5, 15, 2)

#Main game loop
def game_loop():
    global in_combat
    while(True):
        #Exploring
        if not in_combat:
            c = input("Press [E] to explore. \n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if c == "E" or c == "e":
                print("You explore...\n")
                encount = ra.randint(1,3)
                if encount == 1:
                    in_combat = True
                    enemy = Enemy(
                        ra.randint(1,5),
                        ra.randint(10,20),
                        ra.randint(0,3),
                        1,
                        ra.randint(100,200)
                        )
                else:
                    in_combat = False
            else:
                print("Put the correct terms.")
        
        #During Combat
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Enemy Health: {enemy.health}")
            print(f"Player Health: {player.health} Player's Level: {player.lvl} EXP: {player.exp}")
            c = input("\nPress [A] for Attack or [D] for Defend.\n")
            if c == "A" or c == "a":
                enemy.health -= ma.ceil(player.attack * (1 - enemy.defense / 100)) 
                player.health -= ma.ceil(enemy.attack * (1 - player.defense / 100))
                if player.health <= 0:
                    print("You died!")
                    sys.exit()
                if enemy.health <= 0:
                    print("\nYou killed the enemy.")
                    player.exp += enemy.exp
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if player.exp >= player.exp2lvlup():
                        player.lvl += 1
                        player.health += 5
                        player.attack += 2
                        player.defense += 1
                        player.exp = 0
                        print(f"\nCongratulations! You leveled up to {player.lvl}!\n")
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