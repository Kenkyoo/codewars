def make_readable(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    
    if h < 10:
        h = f"0{h}"
    if m < 10:
        m = f"0{m}"
    if s < 10:
        s = f"0{s}"
        
    return f"{h}:{m}:{s}"
        
make_readable(59)

# Explicacion del codigo
# La función make_readable toma un número de segundos como entrada y lo convierte en un formato de tiempo legible (HH:MM:SS).
# Primero, se calcula el número de horas dividiendo los segundos por 3600 (el número de segundos en una hora). Luego, se calcula el número de minutos tomando el resto de los segundos después de calcular las horas y dividiéndolo por 60. Finalmente, se calcula el número de segundos restantes utilizando el operador módulo.
# Después de calcular las horas, minutos y segundos, se verifica si cada uno es menor que 10. Si es así, se agrega un cero al principio para asegurarse de que siempre haya dos dígitos en cada parte del tiempo.
# Finalmente, se devuelve una cadena formateada