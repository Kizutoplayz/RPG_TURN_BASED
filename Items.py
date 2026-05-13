class Item:
    def __init__(self, name, item_type, buy_price, sell_price):
        self.name = name
        self.item_type = item_type
        self.buy_price = buy_price
        self.sell_price = sell_price


class Weapon(Item):
    def __init__(self, name, item_type, buy_price, sell_price, atk_bonus):
        super().__init__(name, item_type, buy_price, sell_price)
        self.atk_bonus = atk_bonus

class Armor(Item):
    def __init__(self, name, item_type, buy_price, sell_price, def_bonus):
        super().__init__(name, item_type, buy_price, sell_price)
        self.def_bonus = def_bonus

HealthPotion = Item("Health Potion", "Consumable", 10, 5)
BasicSword = Weapon("Basic Sword", "Weapon", 50, 40, 3)
BasicArmor = Armor("Basic Armor", "Armor", 70, 60, 5)
BasicCrate = Item("Basic Crate", "Consumable", 100, None)

shop_items = [HealthPotion, BasicSword, BasicArmor, BasicCrate]