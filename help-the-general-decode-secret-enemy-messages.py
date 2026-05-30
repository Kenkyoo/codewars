CACHE_POSICIONES = {}

def decode(message):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,? "
    decoded_message = []
    
    for i, encrypted_char in enumerate(message):
        if encrypted_char not in alphabet:
            decoded_message.append(encrypted_char)
            continue
            
        if i in CACHE_POSICIONES and encrypted_char in CACHE_POSICIONES[i]:
            decoded_message.append(CACHE_POSICIONES[i][encrypted_char])
            continue

        if i not in CACHE_POSICIONES:
            CACHE_POSICIONES[i] = {}
            
        found = False
        for candidate in alphabet:
            test_string = "a" * i + candidate
            ciphered_test = encode(test_string)
            
            char_al_que_cambia = ciphered_test[i]
            CACHE_POSICIONES[i][char_al_que_cambia] = candidate
            
            if char_al_que_cambia == encrypted_char:
                decoded_message.append(candidate)
                found = True
                
        if not found:
            decoded_message.append(encrypted_char)
            
    return "".join(decoded_message)