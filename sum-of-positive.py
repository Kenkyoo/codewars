def positive_sum(arr):
    x = []
    for n in arr:
        if n >= 0:
          x.append(n)
    y = sum(x)
    return y

arr = [1, -4, 7, 12]
positive_sum(arr)

# Explicacion del codigo
# 1. Se define la funcion positive_sum que toma un array como parametro
# 2. Se crea una lista vacia x para almacenar los numeros positivos
# 3. Se recorre el array arr y se agrega cada numero positivo a la lista x
# 4. Se calcula la suma de los numeros positivos en la lista x
# 5. Se retorna la suma

# Ejemplo de uso
# arr = [1, -4, 7, 12]
# positive_sum(arr)
# Output: 20