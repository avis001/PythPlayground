def check_ingredient_match(recipe, ingredients):
    missingIngredients = []
    availableIngredients = set(ingredients)

    for neededIngredient in recipe:
        if neededIngredient not in availableIngredients:
            missingIngredients.append(neededIngredient)

    return 100 - (len(missingIngredients) / len(recipe)) * 100, missingIngredients


def main():
    recipe = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
    ingredients = ["Dragon Scale", "Phoenix Feather", "Troll Tusk"]

    a, b = check_ingredient_match(recipe, ingredients)

    print(a)
    print(b)


main()
