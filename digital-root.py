def digital_root(n):
    while n >= 10:
        n = sum_root(n)
    return n

def sum_root(n):
    return sum(int(x) for x in str(n))

n = 493193
n = 16
n = 942
n = 132189

digital_root(n)

# Explicacion del codigo
# El codigo es una funcion que calcula el digital root de un numero.
# El digital root es la suma de los digitos de un numero hasta que solo queda un digito.
# Por ejemplo, el digital root de 493193 es 29 porque 4 + 9 + 3 + 1 + 9 + 3 = 29.
# La funcion sum_root es una funcion auxiliar que suma los digitos de un numero.
# La funcion digital_root es la funcion principal que calcula el digital root de un numero.