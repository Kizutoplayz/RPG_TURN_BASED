class Item:
    def __init__(self, name, item_type, buy_price, sell_price, rarity):
        self.name = name
        self.item_type = item_type
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.rarity = rarity

class Weapon(Item):
    def __init__(self, name, item_type, buy_price, sell_price, rarity, atk_bonus):
        super().__init__(name, item_type, buy_price, sell_price, rarity)
        self.atk_bonus = atk_bonus

class Armor(Item):
    def __init__(self, name, item_type, buy_price, sell_price, rarity, def_bonus):
        super().__init__(name, item_type, buy_price, sell_price, rarity)
        self.def_bonus = def_bonus

#Shop Items
HealthPotion = Item("Health Potion", "Consumable", 10, 5, "Common")
BasicSword = Weapon("Basic Sword", "Weapon", 50, 40, "Common", 3)
BasicArmor = Armor("Basic Armor", "Armor", 70, 60, "Common", 5)
BasicCrate = Item("Basic Crate", "Consumable", 100, "Common", None)

shop_items = [HealthPotion, BasicSword, BasicArmor, BasicCrate]

#Ores
wood = Item("Wood", "Ore", None, 2, "Common")
stone = Item("Stone", "Ore", None, 2, "Common")
sandstone = Item("Sandstone", "Ore", None, 5, "Uncommon")
rusted_iron = Item("Rusted Iron", "Ore", None, 10, "Uncommon")
iron = Item("Iron", "Ore", None, 20, "Uncommon")
gold = Item("Gold", "Ore", None, 40, "Rare")
zinc = Item("Zinc", "Ore", None, 10, "Common")
ruby = Item("Ruby", "Ore", None, 100, "Epic")
sapphire = Item("Sapphire", "Ore", None, 80, "Rare")
emerald = Item("Emerald", "Ore", None, 90, "Epic")
opal = Item("Opal", "Ore", None, 80, "Rare")
mana_crsytal = Item("Mana Crystal", "Ore", None, 200, "Legendary")
venom_crystal = Item("Venom Crystal", "Ore", None, 400, "Legendary")
serpent_scale = Item("Serpent Scale", "Ore", None, 1000, "Omega")
obsidian = Item("Obsidian", "Ore", None, 90, "Epic")