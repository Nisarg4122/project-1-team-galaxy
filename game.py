import random
import json

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
        self.describe_planet()
        if chance_of_success > self.difficulty * 0.2:
            print("You have now concorded the PLANET!")
            found_item = random.choice(self.treasures)
            player.add_to_inventory(found_item)
        else:
            print("....This planet has to many extra turestials that you cannot defeat")
    #maybe a def about the planet decription
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
#need save and load functions
#use player_inventory.json for save and load
def load_inventory():
    try:
        with open('player_inventory.json', 'r') as file:
            inventory = json.load(file)
        return inventory
    except FileNotFoundError:
        print("Inventory file not found! Creating a new inventory.")
        return {"items": []}

# Function to save inventory data to JSON file
def save_inventory(inventory):
    with open('player_inventory.json', 'w') as file:
        json.dump(inventory, file)
    print("Inventory saved.")

# Function to load inventory data from JSON file
def load_inventory():
    try:
        with open('player_inventory.json', 'r') as file:
            inventory = json.load(file)
        return inventory
    except FileNotFoundError:
        print("Inventory file not found! Creating a new inventory.")
        return {"items": []}

# Function to save inventory data to JSON file
def save_inventory(inventory):
    with open('player_inventory.json', 'w') as file:
        json.dump(inventory, file)
    print("Inventory saved.")

def play_game(player, galaxy):
    while true:
        print("\n--- Game Menu ---")
        print("1. Show Inventory")
        print("2. Explore Galaxy")
        print("3.Save Game")
        print("4. Save Inventory")
        print("5. Exit to Main Menu")
        choice = input("Choose an option: ")
        if choice =="1":
            player.show_inventory()
        elif choice == "2":
            galaxy. show_plantes()
            try:
                planet_choice = int(input("Select a plant to explore:  "))
                if 1 <= planet_choice <= len(galaxy.planets):
                    galaxy.planets[planet_choice = 1].explore(player)
                else:
                        print("\nInvalid planet selection.")
            except ValueError:
                    print("\nPlease enter a valid number.")
        elif choice == "3":
            save_character(player)
        elif choice == "4":
            save_inventory(player.to_dict())
        elif choice == "5":
            print("\nReturning to the main menu..")
            break
        else:
            print("\nInvalid option. Try again.")
            
def main():
    print("Welcome to galaxy explore!")
    while true:
        print("\n--- Main Menu ---")
        print("1. New Game")
        print("2. Load Game")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            player_name = input("\nEnter your name, explorer: ")
            player = Player(player_name)
            galaxy = Galaxy()
            play_game(player, galaxy)
        elif choice == "2":
            player = load_game()
            if player:
                galaxy = Galaxy()
                play_game(player, galaxy)
        elif choice == "3":
            print("\nSee you next time explorer! Safe travels!...watch for the space poop....")
        else:
            print("\nInvalid option. Select again.")
                        