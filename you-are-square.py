def is_square(n):
    if n < 0:
        return False

    x = n**0.5
    return x.is_integer()


is_square(16)
is_square(5)
is_square(-2)

# La funcion is_square toma un numero como parametro y devuelve True si el numero es un cuadrado perfecto y False si no lo es.
