def create_phone_number(n):
    z = "".join(str(x) for x in n[:])
    return f"({z[0:3]}) {z[3:6]}-{z[6:]}"
        
    
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

# La función `create_phone_number` toma una lista de dígitos y los convierte en un número de teléfono con el formato "(XXX) XXX-XXXX". Primero, convierte cada dígito en una cadena y los une para formar una sola cadena de números. Luego, utiliza slicing para formatear la cadena según el formato deseado.