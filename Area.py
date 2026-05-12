class Area:
    def __init__(self, name, map, player_pos):
        self.name = name
        self.map = map
        self.player_pos = player_pos

forest_map = [
    ["S", "S", "G", "G"],
    ["S", "G", "G", "S"],
    ["G", "G", "S", "S"],
]

forest = Area("Forest", forest_map, 0)
print(f"You are in {forest.name}")
print(forest_map)