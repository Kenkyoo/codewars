import string

def rot13(message):
    r = ""

    for x in message:
        if x.islower():
            i = string.ascii_lowercase.index(x)
            r += string.ascii_lowercase[(i + 13) % 26]
        elif x.isupper():
            i = string.ascii_uppercase.index(x)
            r += string.ascii_uppercase[(i + 13) % 26]
        else:
            r += x

    return r

print(rot13("aA bB zZ 1234 *!?%:"))

# Explicacion del codigo
# La función rot13 toma un mensaje como entrada y devuelve una nueva cadena donde cada letra ha sido reemplazada por la letra que se encuentra 13 posiciones adelante en el alfabeto. Si la letra es mayúscula, se mantiene como mayúscula, y si es minúscula, se mantiene como minúscula. Los caracteres que no son letras (como números o símbolos) se dejan sin cambios.
# El código utiliza el módulo string para acceder a las letras del alfabeto. Para cada carácter en el mensaje, se verifica si es una letra mayúscula o minúscula. Si es una letra, se encuentra su índice en el alfabeto y se calcula la nueva posición sumando 13 y tomando el módulo 26 para asegurarse de que se mantenga dentro del rango de las letras. Finalmente, se construye la nueva cadena con los caracteres transformados y se devuelve el resultado.