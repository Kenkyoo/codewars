def find_it(seq):
    for n in seq:
        if seq.count(n) % 2 != 0:
            print(n)
            

seq = [1,2,2,3,3,3,4,3,3,3,2,2,1]

find_it(seq)

# Explicacion el codigo
# El codigo es una funcion que encuentra el numero impar en una lista de numeros.
# La funcion recorre la lista y cuenta la cantidad de veces que aparece cada numero.
# Si el numero aparece un numero impar de veces, se imprime el numero.
# Si el numero aparece un numero par de veces, se ignora.
# La funcion devuelve el numero impar.
# La funcion es O(n) en tiempo y O(1) en espacio.