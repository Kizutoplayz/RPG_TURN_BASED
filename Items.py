class Item:
    def __init__(self, name, item_type):
        self.name = name
        self.item_type = item_type

class Weapon(Item):
    def __init__(self, name, item_type, atk_bonus):
        super().__init__(name, item_type)
        self.atk_bonus = atk_bonus

class Armor(Item):
    def __init__(self, name, item_type, def_bonus):
        super().__init__(name, item_type)
        self.def_bonus = def_bonus

