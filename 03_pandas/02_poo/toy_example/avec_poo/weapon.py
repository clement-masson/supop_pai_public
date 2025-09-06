class Weapon:
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage

    def calculate_damage(self, character) -> int:
        # This method calculates the damage based on the weapon's damage and character's attributes
        if character.equiped_weapon == "shield":
            return self.damage // 10
        return self.damage