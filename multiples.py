def solution(number):
    x = 0
    if number < 1:
        return 0
    for n in range(1, number):
        if n % 3 == 0 or n % 5 == 0:
            x += n
    return x


solution(10)
solution(-2)
solution(0)
solution(25)

# Esta funcion calcula la suma de todos los multiplos de 3 o 5 menores que el numero dado.
# Si el numero es menor que 1, devuelve 0.
# Si el numero es mayor o igual a 1, itera desde 1 hasta el numero dado y suma todos los multiplos de 3 o 5.
# Devuelve la suma total.
