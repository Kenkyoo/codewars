def strip_comments(strng, markers):
    lines = strng.split("\n")
    result = []
    for line in lines:
        for marker in markers:
            if marker in line:
                line = line[:line.index(marker)]
        result.append(line.rstrip())
    return "\n".join(result)

print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))


# Explicación del código:
#
# 1. Separamos el texto en líneas usando split("\n").
#
# 2. Recorremos cada línea por separado.
#
# 3. Para cada línea, asumimos que no hay marcador (cut = len(line)).
#
# 4. Recorremos cada carácter con enumerate para obtener posición (i) y valor (x).
#
# 5. Si encontramos un carácter que está en "markers" (como '#' o '!'),
#    guardamos su posición en "cut" y salimos del bucle.
#
# 6. Cortamos la línea hasta esa posición (line[:cut]) y eliminamos espacios
#    al final con rstrip().
#
# 7. Guardamos la línea limpia en la lista "result".
#
# 8. Finalmente, unimos todas las líneas con "\n" y devolvemos el resultado.
