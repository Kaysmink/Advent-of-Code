from collections import defaultdict
from collections import OrderedDict

Input=open("data/Day 21. input.txt", "r").read().split("\n")[:-1]

countIngredient = defaultdict(int)
AllergieByIngredient = defaultdict(list)
ingredientsPerAllergie = defaultdict(list)

for line in Input:
    ingredients = line.split("(contains ")[0].split(" ")[:-1]
    allergen = line.split("(contains ")[1].replace(",", "").replace(")", "").split(" ")

    for allergie in allergen:
        ingredientsPerAllergie[allergie].append(ingredients)
        
    for ingredient in ingredients:
        countIngredient[ingredient] = countIngredient[ingredient] + 1
        for allergie in allergen:
            AllergieByIngredient[ingredient].append(allergie)

allIngredients = list(countIngredient.keys())

# Deel 1 
possibleIngredientByAllergie = defaultdict()
for allergie, lists in ingredientsPerAllergie.items():
    possible = list(set(lists[0]).intersection(*lists))
    possibleIngredientByAllergie[allergie] = possible   

definitiveIngredientByAllergie = defaultdict()
while True: 
    delete = []
    for key, possibles in possibleIngredientByAllergie.items():
        if len(possibles) == 1:
            definitiveIngredientByAllergie[key] = possibles[0]
            delete.append(possibles[0])
    for key, possibles in possibleIngredientByAllergie.items():
        for values in delete:
            if values in possibleIngredientByAllergie[key]:
                possibleIngredientByAllergie[key].remove(values)
    if len(definitiveIngredientByAllergie.keys()) == len(possibleIngredientByAllergie.keys()):
        break

ingredientsWithoutAllergie = [value for value in allIngredients if value not in definitiveIngredientByAllergie.values()]

result1 = 0
for ingredient in ingredientsWithoutAllergie:
    result1 = result1 + countIngredient[ingredient]

print(result1)

# Deel 2 
definitiveIngredientByAllergie = OrderedDict(sorted(definitiveIngredientByAllergie.items()))

listOfIngredients = []
for allergie, ingredient in definitiveIngredientByAllergie.items():
    listOfIngredients.append(ingredient)

print(",".join(listOfIngredients))