import random as ra, math as ma, sys, os 
from Stat import Player, Enemy
from Items import Item, Weapon, Armor, shop_items, item_lookup
from Areas import list_o_area, enemy_drops
import json

#Player Data
def Name():
    p_name = input("Your Name: ")
    return p_name
player = Player(Name(), 10, 20, 2, )
in_combat = False


#Main game loop
def game_loop():
    global in_combat
    while(True):

#Exploring
        if not in_combat:
            c = input("Press [E] to explore | [P] for profile | [M] for available menus. \n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if c == "E" or c == "e":
                print("You explore...\n")
                encount = ra.randint(1,3)
                if encount == 1:
                    #Creating Enemy
                    enemy = Enemy(
                        ra.choice(player.current_area.enemy_pool),  # name
                        ra.randint(1,5),         # attack
                        ra.randint(10,20),       # health
                        ra.randint(0,3),         # defense
                        1,                       # level
                        ra.randint(100,200),     # exp
                        ra.randint(10,60),       # coin
                        ""                       # drops
                        )
                    enemy.drop = enemy_drops.get(enemy.name, None)
                    in_combat = True
                    
#Mining
                # else:
                #     c = input(print("You found glowing rock. What might it be? Press [M] to mine.\n"))
                #     if c == "Mi" or c == "mi":
                #         print("")

#Crafting
            elif c == "C" or c == "c":
                with open("recipe.json", "r") as f:
                    recipes = json.load(f)
                i = 0
                for recipe_name, details in recipes.items():
                    i += 1
                    print(f"{i}. {recipe_name}: ")
                    for ingredient, amount in details["ingredients"].items():
                        print(f"       {ingredient} x{amount}")
                try:
                    c = input("Choose a number to craft and its quanity: ").split()
                    recipe_name = list(recipes.keys())
                    chosen_name = recipe_name[int(c[0]) -1]
                    chosen = recipes[chosen_name]
                    q = int(c[1]) if len(c) > 1 else 1
                    can_craft = True
                    for ingredient, amount in chosen["ingredients"].items():
                        if player.inventory.get(ingredient, 0) < amount * q:
                            can_craft = False
                            print(f"\nDid you even check your inventory before crafting? You don't have enough items.\n")
                            break
                    if can_craft:
                        for ingredient, amount in chosen["ingredients"].items():
                            player.inventory[ingredient] -= amount * q
                            if player.inventory[ingredient] <= 0:
                                del player.inventory[ingredient]
                        result_item = item_lookup[chosen["result"]]
                        if chosen["result"] in player.inventory:
                            player.inventory[result_item.name] += 1 * q
                        else:
                            player.inventory[result_item.name] = 1 * q
                        print(f"\nYou crafted {q} {chosen_name}")
                except ValueError:
                    print("\nDid you even read? Put numbers.\n")
                except IndexError:
                    print("\nWere you trying to craft a non existent object?\n")

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
                f"Defense: {player.defense}\n"
                f"Current Area: {player.current_area}\n")

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
                    c = input("Input the item number and its quantity to buy[item_number quantity].\n").split()
                    chosen = shop_items[int(c[0]) - 1]
                    b = chosen.buy_price
                    q = int(c[1]) if len(c) > 1 else 1
                    if player.coin >= b * q:
                        if chosen in player.inventory:
                            player.inventory[chosen.name] += 1 * q
                        else:
                            player.inventory[chosen.name] = 1 * q
                        player.coin -= b * q
                        print(f"You purchased {q} {chosen.name}")
                    else:
                        print("You don't have enough coins, you broke kid.")
                except ValueError:
                    print("Put a number, stoooopid.")
                except IndexError:
                    print("Are you even reading the list? There is no such item.")                    

#List of Areas
            elif c == "W" or c == "w":
                print("World Map.")
                print(f"Current Area: {player.current_area.name}")
                for i, area in enumerate(list_o_area, 1):
                    print(f"{i}.{area.name}") 
                try:
                    c = int(input("\nTravel to the areas by pressing the numbers:\n"))
                    chosen = list_o_area[c - 1]
                    if chosen.is_unlocked:
                        player.current_area = chosen
                    else:
                        print("You never even been there, how will you go back to the place where you never went?")
                except TypeError:
                    print("Again, its only numbers.")
                except IndexError:
                    print("You wanna go to narnia or something? Put only the available ones.")



#List of Commands
            elif c == "M" or c == "m":
                print("List of Commands: ")
                print("[I] for Inventory\n"
                      "[S] for Shop\n"
                      "[W] for World Map\n"
                      "[Mi] for Mining\n"
                      "[C] for Crating Menu\n")
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