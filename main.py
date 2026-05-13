import random as ra, math as ma, sys, os 
from Stat import Player, Enemy
from Items import Item, Weapon, Armor, shop_items

#Misc
def Name():
    p_name = input("Your Name: ")
    return p_name
in_combat = False
player = Player(Name(), 10, 20, 2, )
enemy_names = ["Goblin", "Orc", "Troll", "Bandit", "Wolf", "Slime", "Gnome"]
enemy_drops = {
    "Wolf": "Fur",
    "Goblin": "Leather",
    "Orc" : "placeholder",
    "Troll" : "placeholder",
    "Bandit" : "placeholder",
    "Slime" : "Slime Ball",
    "Gnome" : "placeholder",
}

#Main game loop
def game_loop():
    global in_combat
    while(True):

#Exploring
        if not in_combat:
            c = input("Press [E] to explore | [P] for profile | [I] for inventory | [S] for shop. \n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if c == "E" or c == "e":
                print("You explore...\n")
                encount = ra.randint(1,3)
                if encount == 1:
                    in_combat = True
                    enemy = Enemy(
                        ra.choice(enemy_names),
                        ra.randint(1,5),
                        ra.randint(10,20),
                        ra.randint(0,3),
                        1,
                        ra.randint(100,200),
                        ra.randint(10,60),
                        ""
                        )
                    enemy.drop = enemy_drops.get(enemy.name, None)
                else:
                    in_combat = False

#PLayer Profile
            elif c == "P" or c == "p":
                print("Player Profile\n"
                f"Player Name: {player.name}\n"
                f"Level: {player.lvl}\n"
                f"Exp: {player.exp}/{int(player.exp2lvlup())}\n"
                f"Coins: {player.coin}\n"
                f"Special Coins: {player.s_coin}\n"
                f"Health: {player.health}\n"
                f"Attack: {player.attack}\n"
                f"Defense: {player.defense}\n")

#Player Inventory
            elif c == "I" or c == "i":
                print("Inventory: ")
                for k, v in player.inventory.items():
                    print(f"{k} : {v}")

#Shoup
            elif c == "S" or c == "s":
                print("Shooup items:")
                for i, item in enumerate(shop_items, 1):
                    print(f"{i}. {item.name}: {item.buy_price} coins")
                try:    
                    c = int(input("Input the number of the item to buy.\n"))
                    chosen = shop_items[c - 1]
                    if player.coin > chosen.buy_price:
                        if chosen in player.inventory:
                            player.inventory[chosen.name] += 1
                        else:
                            player.inventory[chosen.name] = 1
                        player.coin -= chosen.buy_price
                        print(f"You purchased {chosen.name}")
                    else:
                        print("You don't have enough coins, you broke kid.")
                except ValueError:
                    print("Put a number, stoooopid.")                    
            else:
                print("Put the correct terms.\n")

#During Combat
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Enemy: {enemy.name}")
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
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"\nYou killed the {enemy.name}.")
                    player.exp += enemy.exp
                    print(f"Exp Gained: {enemy.exp}")
                    player.coin += enemy.coin
                    print(f"Coin Gained: {enemy.coin}")
                    item_encount = ra.randint(1,2)
                    if item_encount == 1:
                        print(f"You found an item: {enemy.drop}")
                        if enemy.drop in player.inventory:
                            player.inventory[enemy.drop] += 1
                        else:
                            player.inventory[enemy.drop] = 1
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