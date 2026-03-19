import re

def generate_hashtag(s):
    
    if len(s) <= 0:
        return False
    
    s = re.sub(r'#', '', s)
    s = s.title()
    s = f'#{"".join(s.split())}'
    if len(s) < 140:
        return s
    else:
        return False
    

generate_hashtag(" Hello there thanks for trying my Kata")
generate_hashtag("    Hello     World   " )
generate_hashtag("#Codewars")
generate_hashtag("c i n")

# Explicacion del codigo
# La función generate_hashtag toma una cadena de texto como entrada y genera un hashtag a partir de ella.
# Primero, se verifica si la longitud de la cadena es menor o igual a 0. Si es así, se devuelve False.
# Luego, se eliminan los caracteres '#' de la cadena utilizando re.sub.
# A continuación, se convierte la cadena a formato título utilizando el método title(), lo que capitaliza la primera letra de cada palabra.
# Después, se crea el hashtag concatenando el símbolo '#' con la cadena sin espacios, utilizando "".join(s.split()) para eliminar los espacios.
# Finalmente, se verifica si la longitud del hashtag es menor a 140 caracteres. Si es así, se devuelve el hashtag generado; de lo contrario, se devuelve False. 