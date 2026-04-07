def sum_of_intervals(intervals):
    intervals = sorted(intervals)
    first = [intervals[0]]
    for s, e in intervals[1:]:
        last_s, last_e = first[-1]
        if s <= last_e:
            first[-1] = (last_s, max(last_e, e))
        else:
            first.append((s, e))
    result = 0
    for x in first:
        result += x[1] - x[0]
    return result
        
    
sum_of_intervals([
   [1, 4],
   [7, 10],
   [3, 5]
])

# Explicacion del codigo
# Si no hay intervalos, devolver lista vacía
# Ordenar por el primer -numero
# Empezar por el primer intervalo
# Obtener el ultimo intervalo
# Comparar si se superponer
# De ser true, expandir el ultimo intervalo
# De ser false, agregar como nuevo intervalo
# Calcular la suma de cada intervalo restando el ultimo y el primero de cada uno
