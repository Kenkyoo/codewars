def descending_order(num):
    num = str(num)
    num = sorted(str(num), reverse=True)
    num = "".join(num)
    num = int(num)
    return num

num = 42145
descending_order(num)

# La función descending_order toma un número como entrada y devuelve el número resultante después de ordenar sus dígitos en orden descendente.
# Por ejemplo, si se llama a descending_order(42145), la función devolverá 54421.
# La función convierte el número en una cadena, lo ordena en orden descendente y devuelve el número formateado con los dígitos ordenados.
