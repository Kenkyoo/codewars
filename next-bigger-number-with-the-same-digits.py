def next_bigger(n):
    
    n = list(str(n))
    pivot = 0
    
    for i in range(len(n) - 1, 0, -1):
        if int(n[i]) > int(n[i - 1]):
            pivot = i - 1
            break
    else:
        return -1
        
    right_pivot = sorted(n[pivot+1:])
    
    for i in right_pivot:
        if int(n[pivot]) < int(i):
            x = i
            break
        
    pos = n[pivot+1:].index(x) + pivot + 1
    
    n[pivot], n[pos] = n[pos], n[pivot]
    
    right_side = sorted(n[pivot+1:])
    
    left_side = n[:pivot+1]
    
    return int("".join(left_side + right_side))
    
next_bigger(59884848459853)

# Explicacion del codigo:
#
# 1. Convertir el numero en lista de caracteres para poder manipular cada digito individualmente
#
# 2. Encontrar el "pivote": recorremos la lista de derecha a izquierda buscando el primer digito
#    que sea MENOR que el digito a su derecha. Ese digito es nuestro pivote (el punto donde
#    podemos hacer un cambio para obtener un numero mayor). Si no encontramos ninguno, significa
#    que los digitos estan ordenados de mayor a menor, por lo que retornamos -1
#
# 3. Crear una lista ordenada (right_pivot) con los digitos que estan a la derecha del pivote.
#    Esto nos ayudara a encontrar el numero justo mayor al pivote
#
# 4. Buscar en right_pivot el primer numero que sea MAYOR que el pivote. Ese numero (x) es el
#    que intercambiaremos con el pivote para obtener el siguiente numero mas grande posible
#
# 5. Encontrar la posicion REAL de x dentro de la lista original (no en right_pivot). Para eso:
#    - n[pivot+1:] toma solo la parte derecha original
#    - .index(x) encuentra su posicion dentro de esa parte (0, 1, 2...)
#    - + pivot + 1 convierte esa posicion al indice real en la lista completa
#
# 6. Intercambiar el pivote con x usando sus posiciones reales
#
# 7. Ordenar ascendentemente todos los digitos que quedaron a la derecha del nuevo pivote
#    (esto asegura que sea el numero MAS PEQUEÑO posible entre los que son mayores al original)
#
# 8. Mantener la parte izquierda (hasta el pivote inclusive) sin cambios
#
# 9. Unir ambas partes y convertir a entero para retornar el resultado
#
# Ejemplo con 2017:
# - Lista: [2,0,1,7]
# - Pivote: indice 2 (valor 1) porque 1 < 7
# - x = 7 (el unico mayor que 1 a la derecha)
# - Intercambiar: [2,0,7,1]
# - Ordenar derecha (despues del 7): [1] ya ordenado
# - Resultado: 2071