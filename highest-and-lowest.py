def high_and_low(numbers):
    x = [int(n) for n in numbers.split()]
    x.sort()
    return f'{x[-1]} {x[0]}'
high_and_low("1 2 3 4 5")

# La función high_and_low toma una cadena de números como entrada y devuelve la cadena resultante después de encontrar el número más alto y el más bajo.
# Por ejemplo, si se llama a high_and_low("1 2 3 4 5"), la función devolverá "5 1".
# La función convierte la cadena en una lista de números enteros, los ordena y devuelve la cadena formateada con el número más alto y el más bajo.
