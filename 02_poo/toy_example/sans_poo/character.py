from weapon import calculate_damage
# This code is a simplified version of the character and weapon management system without using classes.








def add_weapon(character: dict, weapon: dict)-> None:
    character["inventory"].append(weapon)

def equip_weapon(character: dict, i: int)-> None:
    character["equiped_weapon"] = character["inventory"][i]

def greet(character: dict)-> None:
    print(f"Hello, my name is {character["name"]} and I am {character["age"]} years old.")

def attack(character: dict, other: dict)-> None:
    if character["equiped_weapon"] is None:
        print(f"{character["name"]} has no weapon equipped.")
        return

    damage = calculate_damage(character["equiped_weapon"], other)
    other["life"] -= damage

if __name__ == "__main__":
    # Example usage
    hero = {"name" : "Hero", "age": 30, "life": 100, "equiped_weapon": None, "inventory": []}
    sword = {"name": "Sword", "damage": 5}
    add_weapon(hero, sword)
    equip_weapon(hero, 0)
    greet(hero)

    villain = {"name": "Villain", "age": 40, "life": 80, "equiped_weapon": None, "inventory": []}
    attack(hero, villain)
    
    print(f"{villain["name"]} has {villain["life"]} life points after the attack.")