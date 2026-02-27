def accum(st):
    y = []
    for i, l in enumerate(st, start=1):
        x = (l * i).capitalize()
        y.append(x)
    return "-".join(y)


accum("abcd")
accum("RqaEzty")
accum("cwAt")

# Esta funcion toma una cadena de texto y devuelve una cadena de texto en la que cada letra se repite el numero de veces igual a su posicion en la cadena original, y se separa por guiones. Por ejemplo, si la entrada es "abcd", la salida sera "A-Bb-Ccc-Dddd".
