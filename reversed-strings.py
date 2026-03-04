def solution(string):
    x = []
    for l in string:
      x.append(l)
    x.reverse()
    x = ''.join(x) 
    return x

solution("world")

# Explicacion del codigo
# 1. Se crea una lista vacia x
# 2. Se recorre la cadena de caracteres string y se agrega cada letra a la lista x
# 3. Se invierte la lista x
# 4. Se convierte la lista x en una cadena de caracteres
# 5. Se retorna la cadena de caracteres