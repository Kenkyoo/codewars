def rgb(r, g, b):
    if r < 0:
        r = 00
    elif r > 255:
        r = 255

    if g < 0:
        g = 00
    elif g > 255:
        g = 255

    if b < 0:
        b = 00
    elif b > 255:
        b = 255
    
    x = f"{r:02x}{g:02x}{b:02x}"
    return x.upper()

rgb(-20, 275, 125)
rgb(255, 255, 255)
rgb(255, 255, 300)


# Explicacion del codigo
#La función rgb toma tres argumentos: r, g y b, que representan los valores de rojo, verde y azul respectivamente.
#Dentro de la función, se verifica si cada valor es menor que 0 o mayor que 255. Si es menor que 0, se asigna el valor 00 (en formato hexadecimal). Si es mayor que 255, se asigna el valor 255.
#Luego, se utiliza una cadena de formato para convertir los valores de r, g y b a su representación hexadecimal. El formato "{:02x}" asegura que cada valor se convierta a un número hexadecimal de dos dígitos, rellenando con ceros si es necesario.
#Finalmente, se devuelve la cadena resultante en mayúsculas utilizando el método upper().