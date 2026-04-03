def solution(args):
    # your code here
    r = []
    start = args[0]
    for i in range(len(args) - 1):
        if not args[i+1] == args[i] + 1:
            if start == args[i]:
                r.append(f"{start}")
                start = args[i+1]
            elif args[i] == start +1:
                r.append(f"{start}")
                r.append(f"{args[i]}")
                start = args[i+1]
            else:
                r.append(f"{start}-{args[i]}")
                start = args[i+1]
    if start == args[-1]:
        r.append(f"{start}")
    elif args[-1] == start +1:
        r.append(f"{start}")
        r.append(f"{args[-1]}")
    else:
        r.append(f"{start}-{args[-1]}")
    return ",".join(r)


solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"

# Explicacion del codigo

# Se recorre la lista de numeros ordenados para detectar grupos de numeros consecutivos.
# La variable "start" guarda el inicio del grupo actual.

# En cada iteracion se compara el numero actual con el siguiente:
# Si NO son consecutivos, significa que el grupo termino.

# Cuando termina un grupo, hay 3 casos:
# 1. Si start == args[i] → el grupo tiene un solo numero → se agrega tal cual.
# 2. Si args[i] == start + 1 → hay 2 numeros → se agregan por separado.
# 3. Si no → hay 3 o mas numeros → se agrega como rango "inicio-fin".

# Luego de procesar el grupo, se actualiza "start" al siguiente numero,
# comenzando un nuevo grupo.

# Al terminar el bucle, queda un ultimo grupo sin procesar,
# por eso se repite la misma logica usando args[-1] como final.

# Finalmente, se unen todos los elementos con comas usando join
# para obtener el string final formateado.
