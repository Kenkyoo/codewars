def is_isogram(string):
    s = string.lower()
    return len(s) == len(set(s))


is_isogram("Dermatoglyphics")
is_isogram("aba")
is_isogram("moOse")
is_isogram("eIAZGRMHRAkuPDu")

# Esta funcion toma una cadena de texto y devuelve True si es un isograma, False en caso contrario.
