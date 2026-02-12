def square_digits(num):
    digits = []
    for n in str(num):
        n = int(n)
        n **= 2
        digits.append(n)
    digits = int("".join(str(n) for n in digits))
    return digits

num = 9119
square_digits(num)

# La función square_digits toma un número entero como entrada y devuelve el número resultante después de elevar cada dígito al cuadrado.
# Por ejemplo, si se llama a square_digits(9119), la función devolverá 811181.
# La función recorre cada dígito del número, lo eleva al cuadrado y lo agrega a una lista. Luego, convierte la lista en un número entero y lo devuelve.
