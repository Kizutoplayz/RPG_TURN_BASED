class Area:
    def __init__(self, name, enc_chance, lvl_req, is_unlocked, boss_defeated, difficulty, ore_pool, enemy_pool):
        self.name = name
       #self.enc_chance = enc_chance
        self.lvl_req = lvl_req
        self.is_unlocked = is_unlocked
        self.boss_defeated = boss_defeated
        self.difficulty = difficulty
        self.ore_pool = ore_pool
        self.enemy_pool = enemy_pool

class Dungeon(Area):
    pass


#Pool of enemies in each Area
forest_enemy_pool = ["Bandit", "Slime", "Wolf"]
whisering_swamp_enemy_pool = ["Orc", "Troll", ]
dwarven_mine_enemy_pool = ["Goblin", "Gnome"]
crytal_canyon_enemy_pool = []
mountain_of_lamia_enemy_pool = []

#Enemy Drops
enemy_drops = {
    "Wolf": "Fur",
    "Goblin": "Leather",
    "Orc" : "placeholder",
    "Troll" : "placeholder",
    "Slime" : "Slime Ball",
    "Gnome" : "placeholder",
}

#Pool of ores in each Area
forest_ore_pool = ["Wood", "Stone"]
whisering_swamp_ore_pool = ["Sandstone", "Rusted Iron"]
dwarven_mine_ore_pool = ["Iron", "Gold", "Zinc"]
crytal_canyon_ore_pool = ["Ruby", "Sapphire", "Emerald", "Opal", "Mana Crystal"]
mountain_of_lamia_ore_pool = ["Venom Crystal", "Serpent Scale", "Obsidian"]


#Areas
forest = Area("Forest", 1, 1, True, True, 1, forest_ore_pool, forest_enemy_pool)
whisering_swamp = Area("Whispering Swamp", 1, 20, True, True, 1, whisering_swamp_ore_pool, whisering_swamp_enemy_pool)
dwarven_mine = Area("Drawven Mine", 1, 50, True, True, 1, dwarven_mine_ore_pool, dwarven_mine_enemy_pool)
crytal_canyon = Area("Crystal Canyon", 1, 80, True, True, 1, crytal_canyon_ore_pool, crytal_canyon_enemy_pool)
mountain_of_lamia = Area("Mountain of Lamia", 1, 100, True, True, 1, mountain_of_lamia_ore_pool, mountain_of_lamia_enemy_pool)

list_o_area = [forest, whisering_swamp, dwarven_mine, crytal_canyon, mountain_of_lamia]