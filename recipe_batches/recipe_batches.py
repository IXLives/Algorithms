#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    portions = 0
    prevPortion = 0
    portionLowest = 0
    for key in recipe:
        prevPortion = portions
        if key in ingredients:
            portions = ingredients[key] // recipe[key]
            if portions < portionLowest:
                portionLowest = portions
                return portionLowest
            if portions == 0:
                return('Zero')
            else:
                return portions
        else:
            return('Zero')


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
