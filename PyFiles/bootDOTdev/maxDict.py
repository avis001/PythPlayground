def get_most_common_enemy(enemies_dict):
    max = float("-inf")
    ene = None

    for eachEi in enemies_dict:
        if enemies_dict[eachEi] > max:
            max = enemies_dict[eachEi]
            ene = eachEi

    return ene
