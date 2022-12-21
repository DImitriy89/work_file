import os
file_name = os.path.join(os.getcwd(), 'recipes.txt')
from pprint import pprint
#задача 1
def recipes_reader(file_name: str) -> dict:
    with open(file_name, encoding='utf-8') as f:
        dict_recipes = {}
        for line in f:
            dish_name = line.strip()
            dict_recipes[dish_name] = []
            quantity =f.readline().strip()
            for item in range (int(quantity.strip())):
                ingredient = {}
                obj =f.readline()
                obj = obj.strip().replace('|', '')
                obj = obj.split()
                if len(obj) == 3:
                    ingredient['ingredient_name'] = obj[0]
                    ingredient['quantity'] = int(obj[1])
                    ingredient['measure'] = obj[2]
                else:
                    ingredient['ingredient_name'] = obj[0] + ' ' + obj[1]
                    ingredient['quantity'] = int(obj[2])
                    ingredient['measure'] = obj[3]
                dict_recipes[dish_name].append(ingredient)
            f.readline()
        return dict_recipes
pprint(recipes_reader('recipes.txt'))
