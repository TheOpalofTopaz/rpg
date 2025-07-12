import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 20
        self.gold = 0
        self.inventory = []

    def is_alive(self):
        return self.hp > 0

class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

def encounter_monster(player):
    monsters = [
        Monster("Goblin", 10, 4),
        Monster("Skeleton", 8, 3),
        Monster("Orc", 14, 5)
    ]
    monster = random.choice(monsters)
    print(f"A wild {monster.name} appears!")

    while monster.is_alive() and player.is_alive():
        action = input("Fight (f) or Run (r)? ").lower()
        if action == "f":
            damage = random.randint(2, 6)
            monster.hp -= damage
            print(f"You hit the {monster.name} for {damage} damage.")
            if monster.is_alive():
                monster_damage = monster.attack
                player.hp -= monster_damage
                print(f"{monster.name} hits you for {monster_damage} damage. Your HP: {player.hp}")
            else:
                print(f"You defeated the {monster.name}!")
                loot = random.randint(5, 20)
                player.gold += loot
                print(f"You found {loot} gold. Total gold: {player.gold}")
        elif action == "r":
            if random.random() < 0.5:
                print("You successfully ran away!")
                return
            else:
                print("Failed to run away!")
                monster_damage = monster.attack
                player.hp -= monster_damage
                print(f"{monster.name} hits you for {monster_damage} damage. Your HP: {player.hp}")
        else:
            print("Invalid action.")

def find_treasure(player):
    treasures = ["Potion", "Sword", "Shield"]
    treasure = random.choice(treasures)
    print(f"You found a {treasure}!")
    player.inventory.append(treasure)

def explore_room(player):
    print("You enter a dark room...")
    event = random.choice(["monster", "treasure", "empty"])
    if event == "monster":
        encounter_monster(player)
    elif event == "treasure":
        find_treasure(player)
    else:
        print("The room is empty.")

def main():
    print("Welcome to the Text RPG!")
    name = input("Enter your character's name: ")
    player = Player(name)

    while player.is_alive():
        print("\n-----")
        print(f"HP: {player.hp}, Gold: {player.gold}, Inventory: {player.inventory}")
        action = input("Explore (e), Rest (r), or Quit (q): ").lower()
        if action == "e":
            explore_room(player)
        elif action == "r":
            heal = random.randint(2, 6)
            player.hp += heal
            print(f"You rest and recover {heal} HP. HP: {player.hp}")
        elif action == "q":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action.")

    if not player.is_alive():
        print("You have perished in your adventure.")

if __name__ == "__main__":
    main()