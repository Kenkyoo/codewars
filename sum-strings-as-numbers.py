def sum_strings(x, y):
    
    str1 = x[::-1]
    str2 = y[::-1]
    max_len = max(len(str1), len(str2))
    
    result = []
    carry = 0
    
    for i in range(max_len):
        dig1 = int(str1[i]) if i < len(str1) else 0
        dig2 = int(str2[i]) if i < len(str2) else 0
        
        suma = dig1 + dig2 + carry
        
        digit_result = suma % 10
        carry = suma // 10
        
        result.append(str(digit_result))
    
    if carry:
        result.append(str(carry))
    
    return ''.join(result[::-1]).lstrip('0') or '0'
        
sum_strings("122", "592")

# Explicación del código:
#
# 1. Invertimos las strings:
#    str1 = x[::-1], str2 = y[::-1]
#    Esto nos permite sumar desde el último dígito (como en papel).
#
# 2. Recorremos ambas strings con un for:
#    Usamos max_len para asegurarnos de recorrer la más larga.
#
# 3. Obtenemos cada dígito:
#    ord(char) - 48 convierte el carácter ('0'-'9') en número (0-9).
#    Si una string es más corta, usamos 0.
#
# 4. Sumamos:
#    suma = dig1 + dig2 + carry
#    carry es el "llevar" de la suma anterior.
#
# 5. Guardamos el resultado:
#    suma % 10 → el dígito actual
#    suma // 10 → el nuevo carry
#
# 6. Si al final queda carry, lo agregamos.
#
# 7. Invertimos el resultado:
#    result[::-1] porque lo construimos al revés.
#
# 8. Limpiamos ceros a la izquierda:
#    lstrip('0') los elimina
#    or '0' asegura que si queda vacío, devolvemos "0"
#
# Resultado:
#    Funciona con números grandes sin usar int()