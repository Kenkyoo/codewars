def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    u = [
        ("year", 31536000),
        ("day", 86400),
        ("hour", 3600),
        ("minute", 60),
        ("second", 1)
    ]
    
    r = []
    
    for l, n in u:
        x = seconds // n
        if x > 0:
            if x == 1:
                r.append(f"{x} {l}")
            else:
                r.append(f"{x} {l}s")
            seconds %= n
    
    if len(r) == 1:
        return r[0]
    elif len(r) == 2:
        return " and ".join(r)
    else:
        return ", ".join(r[:-1]) + " and " + r[-1]
    
# Explicación:
# - Se define una lista de unidades de tiempo con su valor en segundos.
# - Se recorre cada unidad y se calcula cuántas veces entra en el tiempo dado.
# - Si la cantidad es mayor a 0, se agrega al resultado (con plural si corresponde).
# - Se actualiza el valor de segundos con el resto para seguir calculando.
# - Finalmente, se formatea la lista en un string:
#   - 1 elemento → se devuelve directo
#   - 2 elementos → se unen con "and"
#   - más de 2 → comas + "and" al final