def snail(snail_map):
    result = []
    
    while any(snail_map):
        if len(snail_map) == 1:
            result.extend(snail_map[0])
            break
        
        if len(snail_map[0]) == 1:
            for snail in snail_map:
                result.append(snail[0])
            break
        
        y = []
        z = []
        
        y.extend(snail_map[0][0:-1])
        
        for snail in snail_map:
            y.append(snail[-1])
            
        y.extend(snail_map[-1][1:-1][::-1])
        
        for snail in snail_map:
            z.append(snail[0])
            
        z.reverse()
        z = z[0:-1]
        
        x = []
        snail_map = snail_map[1:-1]
        
        for snail in snail_map:
            x.append(snail[1:-1])
            
        snail_map = x
        
        result += y + z

    return result
    
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

snail(array) #=> [1,2,3,6,9,8,7,4,5]

# EXPLICACIÓN DEL Codigo:
# 1. El algoritmo utiliza un bucle 'while' que se ejecuta mientras la matriz tenga elementos.
# 2. Casos base: Si la matriz queda de 1xN o Nx1, se agregan los elementos restantes y termina.
# 3. Recorrido perimetral: 
#    - La lista 'y' captura la fila superior, la columna derecha y la fila inferior (invertida).
#    - La lista 'z' captura la columna izquierda de abajo hacia arriba.
# 4. Reducción de la matriz: Después de completar el "anillo" exterior, el código crea 
#    una nueva matriz 'x' eliminando las filas y columnas ya procesadas.
# 5. El proceso se repite con la matriz interna hasta que no quedan más capas, 
#    acumulando todos los valores en la lista 'result'.