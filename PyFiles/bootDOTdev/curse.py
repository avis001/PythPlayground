def curse(weapon_damage):
    lesserCursed = weapon_damage * (1 - 0.5)
    greaterCursed = weapon_damage * (1 - 0.75)

    return lesserCursed, greaterCursed


# Don't modify below this line


def test(weapon_damage):
    print("Weapon's base damage:", float(weapon_damage))
    print("Cursing...")
    lesser_cursed, greater_cursed = curse(weapon_damage)
    print("With lesser curse the damage is:", float(lesser_cursed), "damage.")
    print("With greater curse the damage is:", float(greater_cursed), "damage.")
    print("=====================================")


def main():
    test(100)
    test(500)
    test(1000)


main()
