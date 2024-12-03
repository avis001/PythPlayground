def calculate_flurry_crit(num_attacks, base_damage):
    finalDamage = 0
    attacksLeft = num_attacks

    while attacksLeft > 0:
        if attacksLeft == 1:
            finalDamage += base_damage * 4
        else:
            finalDamage += base_damage * 2

    return finalDamage
