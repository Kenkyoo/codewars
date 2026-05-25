def spiralize(size):
    lst = [[0] * size for _ in range(size)]
    
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    r, c, d = 0, 0, 0
    
    prev_r, prev_c = -1, -1

    while True:
        lst[r][c] = 1
        
        dr, dc = dirs[d]
        next_r = r + dr
        next_c = c + dc
        
        
        if (next_r < 0 or next_r >= size or next_c < 0 or next_c >= size or lst[next_r][next_c] == 1):
            girar = True
        else:

            vecinos_con_uno = 0
            for nr, nc in [(next_r+1, next_c), (next_r-1, next_c), (next_r, next_c+1), (next_r, next_c-1)]:
                if 0 <= nr < size and 0 <= nc < size and lst[nr][nc] == 1:
                    vecinos_con_uno += 1
            

            if vecinos_con_uno > 1:
                girar = True
            else:
                girar = False

        if girar:
            
            d = (d + 1) % 4
            dr, dc = dirs[d]
            next_r = r + dr
            next_c = c + dc
            
            
            if (next_r < 0 or next_r >= size or next_c < 0 or next_c >= size or lst[next_r][next_c] == 1):
                break
                
            
            vecinos_con_uno = 0
            for nr, nc in [(next_r+1, next_c), (next_r-1, next_c), (next_r, next_c+1), (next_r, next_c-1)]:
                if 0 <= nr < size and 0 <= nc < size and lst[nr][nc] == 1:
                    vecinos_con_uno += 1
            if vecinos_con_uno > 1:
                break

        
        r, c = next_r, next_c
        
    return lst
    
spiralize(5)

# 1. Crear la matriz inicial de ceros
# Direcciones tradicionales: Derecha, Abajo, Izquierda, Arriba
# Guardamos la posición anterior para las validaciones
# ¿El siguiente paso se sale de la matriz o toca un 1?
# Si el paso es válido dentro de la matriz, chequeamos la regla de "no tocarse".
# Contamos cuántos '1' rodean a esa celda 'next_r, next_c'
# Como la celda de la que venimos (r, c) ya es un '1', ese vecino es legal.
# Pero si tiene MÁS de un vecino con '1', significa que va a chocar con otra pared.
# Giramos 90 grados a la derecha
# Si después de girar tampoco podemos avanzar, la espiral terminó en el centro
# Validamos que el nuevo camino tras girar no viole la regla de vecinos
# Avanzamos al siguiente casillero