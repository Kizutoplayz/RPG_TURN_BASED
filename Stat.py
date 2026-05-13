import random as ra

#Stats for player and enemies
class Stats:
    def __init__(self, name, attack, health, defense, lvl= 1, exp=0, coin=0, s_coin=0):               
        self.name = name
        self.attack = attack
        self.health = health
        self.defense = defense
        self.lvl = lvl
        self.exp = exp
        self.coin = coin
        self.s_coin = s_coin

class Player(Stats):
    def exp2lvlup(self):
        offset = ra.randint(1,10) / 10
        exp_2_lvlup = 100 * (self.lvl ** (1.2 + offset))
        return exp_2_lvlup
    inventory = {}

class Enemy(Stats):
    def __init__(self, name, attack, health, defense, lvl= 1, exp=0, coin=0, s_coin=0, drop=None):
        super().__init__(name, attack, health, defense, lvl,exp , coin, s_coin)
        self.drop = drop