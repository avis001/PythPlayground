def meditate(mana, max_mana, energy, energy_potions):
    while mana < max_mana and (energy > 0 or energy_potions > 0):
        if energy == 0:
            energy_potions -= 1
            energy += 50

        energy -= 1
        mana += 3
        mana = min(mana, max_mana)

    return mana, energy, energy_potions
