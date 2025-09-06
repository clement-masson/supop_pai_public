def calculate_damage(weapon, character) -> int:
    # This method calculates the damage based on the weapon's damage and character's attributes
    if character["equiped_weapon"] == "shield":
        return weapon["damage"] // 10
    return weapon["damage"]

