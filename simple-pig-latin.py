def pig_it(text):
    x = text.split()
    r = []
    for p in x:
        l = list(p)
        l.append(l.pop(0))
        if p.isalpha():
            l.append("ay")
        r.append("".join(l))
    return " ".join(r)
        
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

# Explicacion del codigo
# La función pig_it toma una cadena de texto como entrada y la convierte a Pig Latin.
# Primero, se divide el texto en palabras utilizando el método split() y se almacena en la variable x.
# Luego, se crea una lista vacía r para almacenar las palabras convertidas.
# Se itera sobre cada palabra p en la lista x. Para cada palabra, se convierte en una lista de caracteres l.
# Se mueve el primer carácter al final de la lista utilizando pop(0) y append().
# Si la palabra es alfabética (es decir, no contiene caracteres especiales), se agrega "ay" al final de la lista l.
# Finalmente, se unen los caracteres de la lista l para formar la palabra convertida y se agrega a la lista r