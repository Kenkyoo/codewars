def get_middle(s):
    x = len(s) // 2

    if len(s) % 2 == 0:
        return s[x - 1] + s[x]
    else:
        return s[x]


s = "test"
si = "testing"

get_middle(si)
get_middle(s)

# Esta funcion recibe una cadena de texto y devuelve el caracter central de la cadena.
# Si la cadena tiene un numero par de caracteres, devuelve los dos caracteres centrales.
# Si la cadena tiene un numero impar de caracteres, devuelve el caracter central.
