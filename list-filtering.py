l = [1,2,'a','b']

def filter_list(l):
    y = []
    for x in l:
        if isinstance(x, int):
            y.append(x)
    return y
filter_list(l)

# El codigo define una lista llamada 'l' que contiene una mezcla de enteros y cadenas de texto. Luego, se define una función llamada 'filter_list' que toma una lista como argumento. Dentro de la función, se crea una nueva lista vacía llamada 'y'. La función itera a través de cada elemento 'x' en la lista 'l', y si el tipo de 'x' es un entero (int), se agrega a la lista 'y'. Finalmente, la función imprime la lista 'y', que contiene solo los enteros de la lista original.