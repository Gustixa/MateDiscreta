codification = {
    "A" : "00", "B" : "01", "C" : "02", "D" : "03", "E" : "04", "F" : "05", "G" : "06", "H" : "07", "I" : "08", "J" : "09", "K" : "10", "L" : "11",
    "M" : "12", "N" : "13", "O" : "14", "P" : "15", "Q" : "16", "R" : "17", "S" : "18", "T" : "19", "U" : "20", "V" : "21", "W" : "22", "X" : "23",
    "Y" : "24", "Z" : "25", "0" : "26", "1" : "27", "2" : "28", "3" : "29", "4" : "30", "5" : "31", "6" : "32", "7" : "33", "8" : "34", "9" : "35",
}

codif_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def main() -> None:

    print(rsa_encryption("ENCRYPTION", 53, 71, 9))
    print(rsa_encryption("STOP", 43, 59, 13))
    print(rsa_encryption("ATTACK", 43, 59, 13))
    print(rsa_encryption("UPLOAD", 53, 61, 17))

    print(rsa_decryption("0632 2142 2415 1590 0734", 53, 71, 9))
    print(rsa_decryption("2081 2182", 43, 59, 13))        
    print(rsa_decryption("1191 1906 2497 0709", 43, 59, 13))        
    print(rsa_decryption("0667 1947 0671", 43, 59, 13))    

    print(vigenere_cipher("OIKYWVHBX", "HOT"))


def rsa_encryption(m, p, q, e):
    m = m.upper()
    n = p * q
    
    blocks = []
    element = ""
    i = 1
    for c in m:
        if c != " ":
            element += str(codification[c])
            if i % 2 == 0:
                blocks.append(int(element))
                element = ""
            i += 1
    message_encrypted = []
    for b in blocks:
        part_encrypted = pow(b, e) % n
        message_encrypted.append(str(part_encrypted)) if len(str(part_encrypted)) == 4 else message_encrypted.append("0" + str(part_encrypted))
             
    return f"+ {m} : " + " ".join(message_encrypted)


def rsa_decryption(c, p, q, e):
    delta = (p - 1) * (q - 1)
    n = p * q
    c = c.split(" ")
    
    # Conseguir llave privada
    key = euclid_extended(e, delta)
    
    # Se utilizará algoritmo de exponenciaión modular
    the_chars_key = list(codification.keys())
    the_numbers_value = list(codification.values())
    letters = []
    for i in c:
        see = pow(int(i), key) % n

        # Si dado caso una letra con el valor de solo un número (una unidad)
        if len(str(see)) != 4:
            see = "0" + str(see)
            if len(str(see)) != 4: # Por sí dado caso termina siendo una letra "A" 
                see = "0" + str(see)
                
        # Se obtendrán las letras encontradas para revelar el mensaje encriptado
        see = str(see)
        letter1 = see[0] + see[1]
        letter2 = see[2] + see[3]

        # Concatenar las letras reveladas                    
        letters.append(the_chars_key[the_numbers_value.index(letter1)])
        letters.append(the_chars_key[the_numbers_value.index(letter2)])

    return f"- C {c} ; Llave privada [{key}], mensaje desencriptado: " + "".join(letters)


def euclid_extended(a, b):
    nums = [1, 0, 0, 1]
 
    while b != 0:
        temp1 = a // b
        temp2 = a - b * temp1
        temp3 = nums[0] - temp1 * nums[1]
        temp4 = nums[2] - temp1 * nums[3]
        a = b
        b = temp2
        nums[0] = nums[1]
        nums[1] = temp3
        nums[2] = nums[3]
        nums[3] = temp4
 
    return nums[0]
 

def vigenere_cipher(code, key):
    code_numbers = []
    for c in code:
        code_numbers.append(codification[c])
    i = 0
    next = 0
    key_numbers = []
    while next != len(code_numbers):                
        key_numbers.append(codification[key[i]])
        i += 1
        i %= len(key)
        next += 1
    
    secret_string = []
    for i in range(len(code_numbers)):
        number_add = (int(code_numbers[i]) - int(key_numbers[i])) % 26        
        secret_string.append(codif_letters[number_add])    

    return f"Mensaje [{code}], Llave [{key}], Codigo Secreto: " + "".join(secret_string)

if __name__ == "__main__":
    main()