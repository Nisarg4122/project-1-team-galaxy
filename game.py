import random

class Player:
    def __init__(self, name, inventory = None):
        self.name = name
        self.health = 100
        self.inventory = inventory if inventory else[]
    def show_inventory(self):
        if self.inventory:
            print(f"\n{self.name}'s Inventory:")
            for i, item in enumerate(self.inventory, 1):
                print(f"{i}. {item}")
        else:
            print("No Inventory")
    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"you picked up: {item}")
    def to_dict(self):
        return {"name": self.name, "inventory": self.inventory}
class Planet:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self. treasures = ["Plasma Shield", "Laser Sword", "Alien Blaster"]
    def explore(self, player):
        print(f"You have arrived on {self.name} (With a difficulty of: {self.difficulty})")
        if chance_of_success > self.difficulty * 0.2:
            print("You have now concorded the PLANET!")
            found_item = random.choice(self.treasures)
            player.add_to_inventory(found_item)
        else:
            print("....This planet has to many extra turestials that you cannot defeat")
class Galaxy:
    def __init__(self):
        self.planets = [
            Planet("Nebula", 1),
            Planet("Area 151", 2),
            Planet("Drull", 3),
        ]
    def show_planets(self):
        print("Planets among this galaxy:")
        for i, planet in enumerate(self.planets, 1):
            print(f"{i}. {planet.name} (Difficulty: {planet.difficulty})")
                       