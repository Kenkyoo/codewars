def array_diff(a, b):
    for x in b:
        while x in a:
            a.remove(x)
    return a

a = [1, 2, 2, 2, 3]
b = [2]

array_diff(a, b)

# Explicacion del codigo
# Recorre cada elemento de la lista b.
# Mientras ese elemento exista en la lista a, lo elimina.
# Al final devuelve la lista a sin los valores que estaban en b.