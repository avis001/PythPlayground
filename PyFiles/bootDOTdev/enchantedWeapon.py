def enchant_and_attack(target_health, damage, weapon):
    enchantedDamage = damage + 10
    newHealth = target_health - enchantedDamage
    enchantedWeapon = f"enchanted {weapon}"

    return enchantedWeapon, newHealth


# Don't modify below this line


def test(target_health, damage, weapon):
    print("The target has", target_health, "health.")
    print(weapon, "base damage:", damage, "Enchanting and attacking")
    enchanted_weapon, new_health = enchant_and_attack(target_health, damage, weapon)
    print("The target has been attacked with the", enchanted_weapon)
    print("The target has", new_health, "health remaining.")
    print("=====================================")


def main():
    test(100, 50, "sword")
    test(500, 100, "axe")
    test(1000, 250, "bow")


main()
