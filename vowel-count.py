lista = ["a", "e", "i", "o", "u"]

def get_count(sentence):
    count = 0

    for letra in sentence:
        if letra in lista:
            count += 1

    return count

# Usa un bucle for para recorrer cada letra de la frase, un if para comprobar si es vocal y un contador que se incrementa cuando encuentra una.