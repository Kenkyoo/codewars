vocals = ["a", "e", "i", "o", "u"]

def disemvowel(string_):
    x = ""
    for i in range(len(string_)):
        if string_[i].lower() not in vocals:
            x += string_[i]
    return x

disemvowel("Hola mundo")
# La función disemvowel toma una cadena como entrada y devuelve la cadena resultante después de eliminar todas las vocales.
# Por ejemplo, si se llama a disemvowel("Hola mundo"), la función devolverá "Hl mnd".
# La función recorre cada carácter de la cadena y lo agrega a una nueva cadena si no es una vocal.
# Finalmente, devuelve la nueva cadena sin vocales.
