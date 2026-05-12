import random as ra

#Stats for player and enemies
class Stats:
    def __init__(self, attack, health, defense, lvl= 1, exp=0):               
        self.attack = attack
        self.health = health
        self.defense = defense
        self.lvl = lvl
        self.exp = exp

class Player(Stats):
    def exp2lvlup(self):
        offset = ra.randint(1,10) / 10
        exp_2_lvlup = 100 * (self.lvl ** (1.2 + offset))
        return exp_2_lvlup
    

class Enemy(Stats):
    pass