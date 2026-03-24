def cakes(recipe, available):

    for k in recipe:
        if k not in available:
            return 0
        else:
            return min(available[k] // recipe[k] for k in recipe)

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}

cakes(recipe, available)

recipe = {'nuts': 34, 'butter': 58, 'crumbles': 91}
available = {'chocolate': 7892, 'nuts': 6479, 'butter': 717, 'cocoa': 5271, 'oil': 4488, 'sugar': 4028, 'pears': 9609, 'flour': 5031, 'cream': 1258, 'crumbles': 616}

cakes(recipe, available)

# Explicacion del codigo
# La función cakes toma dos diccionarios como argumentos: recipe (receta) y available (disponible). 
# La función itera sobre cada ingrediente en la receta y verifica si está presente en el diccionario de ingredientes disponibles. 
# Si algún ingrediente de la receta no está disponible, la función devuelve 0, indicando que no se pueden hacer pasteles. 
# Si todos los ingredientes de la receta están disponibles, la función calcula cuántos pasteles se pueden hacer con los ingredientes disponibles utilizando una comprensión de lista. 
# Para cada ingrediente en la receta, se divide la cantidad disponible por la cantidad requerida en la receta y se toma el mínimo de estos valores para determinar cuántos pasteles se pueden hacer en total. 
# Finalmente, la función devuelve el número máximo de pasteles que se pueden hacer con los ingredientes disponibles.