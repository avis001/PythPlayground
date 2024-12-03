def regenerate(current_health, max_health, enemy_distance):
    updatedHealth = current_health
    updatedEnemyDistance = enemy_distance
    while updatedHealth < max_health and updatedEnemyDistance > 3:
        updatedHealth += 1
        updatedEnemyDistance -= 2

    return updatedHealth
