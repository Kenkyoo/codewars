def move_zeros(lst):
    y = []
    if 0 in lst:
        for x in lst[:]:
            if x == 0:
                lst.remove(x), y.append(x)
    lst += y
    print(lst)

move_zeros([1, 0, 0, 2])

# Explicacion del codigo
# La función move_zeros toma una lista como argumento. Primero, se crea una lista vacía llamada y para almacenar los ceros encontrados en la lista original. Luego, se verifica si hay ceros en la lista utilizando la condición if 0 in lst. Si hay ceros, se itera sobre una copia de la lista original (lst[:]) para evitar modificar la lista mientras se itera. Si se encuentra un cero, se elimina de la lista original utilizando lst.remove(x) y se agrega a la lista y utilizando y.append(x). Finalmente, se concatenan los ceros almacenados en y al final de la lista original utilizando lst += y, y se imprime la lista resultante.