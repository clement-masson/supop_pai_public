from weapon import Weapon

class Character:
    def __init__(self, name: str, age: int, life: int = 100):
        self.name = name
        self.age = age
        self.life = life
        self.equiped_weapon = None # l'arme utilisée lors de l'attaque
        self.inventory = [] # une liste de Weapons

    def add_weapon(self, weapon: Weapon)-> None:
        self.inventory.append(weapon)

    def equip_weapon(self, i: int)-> None:
        self.equiped_weapon = self.inventory[i]

    def greet(self)-> None:
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def attack(self, character)-> None:
        if self.equiped_weapon is None:
            print(f"{self.name} has no weapon equipped.")
            return

        damage = self.equiped_weapon.calculate_damage(character)
        character.life -= damage

if __name__ == "__main__":
    # Example usage
    hero = Character("Hero", 30)
    sword = Weapon("Sword", 5)
    hero.add_weapon(sword)
    hero.equip_weapon(0)
    hero.greet()
    
    villain = Character("Villain", 40, 80)
    hero.attack(villain)
    
    print(f"{villain.name} has {villain.life} life points after the attack.")