##################################################################################################################################################
__author__ = "Cristian Fernando Laynez Bachez"
__copyright__ = "Copyright 2021 - Universidad del Valle de Guatemala"
__credits__ = "Matemática Discreta"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = ["cristianlaynezbachez@gmail.com", "lay201281@uvg.edu.gt"]
__status__ = "Student of Computer Science"

# Proyecto Corto #3 - Criptografía ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# -> Encriptación RSA: 
# -> Desencriptación RSA: 
# -> Vigénere cipher: 
#################################################################################################################################################

# -----------------------------------------------------------------------------------------------------------------------------------------------
# --> Codificación para encriptar/desencriptar --------------------------------------------------------------------------------------------------
codification = {
    "A" : "00", "B" : "01", "C" : "02", "D" : "03", "E" : "04", "F" : "05", "G" : "06", "H" : "07", "I" : "08", "J" : "09", "K" : "10", "L" : "11",
    "M" : "12", "N" : "13", "O" : "14", "P" : "15", "Q" : "16", "R" : "17", "S" : "18", "T" : "19", "U" : "20", "V" : "21", "W" : "22", "X" : "23",
    "Y" : "24", "Z" : "25", "0" : "26", "1" : "27", "2" : "28", "3" : "29", "4" : "30", "5" : "31", "6" : "32", "7" : "33", "8" : "34", "9" : "35",
}

codif_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# -----------------------------------------------------------------------------------------------------------------------------------------------
# --> Función para ejecutar el programa entero --------------------------------------------------------------------------------------------------
def main() -> None:
    print("-------------------------------------------------------------------------------------")
    print("----------------------------------PROYECTO CORTO #3----------------------------------")  
    
    print("\n--> Encriptación RSA: ------------------------------------------------------------\n") # m, p, q, e
    print(rsa_encryption("ENCRYPTION", 53, 71, 9))
    print(rsa_encryption("STOP", 43, 59, 13))
    print(rsa_encryption("ATTACK", 43, 59, 13))
    print(rsa_encryption("UPLOAD", 53, 61, 17))

    print("\n--> Desencriptación RSA: ---------------------------------------------------------\n") # c, p, q, e
    print(rsa_decryption("0632 2142 2415 1590 0734", 53, 71, 9))
    print(rsa_decryption("2081 2182", 43, 59, 13))        
    print(rsa_decryption("1191 1906 2497 0709", 43, 59, 13))        
    print(rsa_decryption("0667 1947 0671", 43, 59, 13))    
            
    print("\n--> Vigénere Cipher: -------------------------------------------------------------\n")
    print(vigenere_cipher("OIKYWVHBX", "HOT"))

    print("\n-----------------------------------FIN PROGRAMA :)-----------------------------------")
    print("-------------------------------------------------------------------------------------")

# -----------------------------------------------------------------------------------------------------------------------------------------------
# --> Encriptación RSA --------------------------------------------------------------------------------------------------------------------------
# @param m: Mensaje a encritar
# @param p: Número primo impar 1
# @param q: Número primo impar 2
# @param e: Número entero tal que e > 1 primo relativo con (p-1)(q-1)
# @return C [str]: Mensaje encriptado
def rsa_encryption(m : str, p : int, q : int, e : int) -> str:
    m = m.upper()
    n = p * q
    
    # Codificiar el mensaje secreto
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

    # Mostrar elementos del bloque    
    message_encrypted = []
    for b in blocks:
        part_encrypted = pow(b, e) % n
        message_encrypted.append(str(part_encrypted)) if len(str(part_encrypted)) == 4 else message_encrypted.append("0" + str(part_encrypted))
             
    return f"+ {m} : " + " ".join(message_encrypted)

# -----------------------------------------------------------------------------------------------------------------------------------------------
# --> Desencriptación RSA -----------------------------------------------------------------------------------------------------------------------
# @param c: Mensaje encriptado
# @param n: Encontrar la llave privada d
# @param e: Desencriptar el mensaje
# @return d & m [str]: Llave privada & mensaje encriptado
def rsa_decryption(c : int, p : int, q : int, e : int) -> str:
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

# --> Algoritmo de euclides extendido (Función auxiliar para obtener llavo privada en [rsa_decryption]) -----------------------------------------
# @param a: Valor e 
# @param b: Valor delta
# @return int: La llave privada de los valores ingresados
def euclid_extended(a : int, b : int) -> int:
    nums = [1, 0, 0, 1]
 
    while b != 0: # Mientras b no sea igual a "b" la iteracion continuara
        # Se llevará a cabo la busqueda
        temp1 = a // b
        temp2 = a - b * temp1
        temp3 = nums[0] - temp1 * nums[1]
        temp4 = nums[2] - temp1 * nums[3]
        # Se actualizaran los valores a y b
        a = b
        b = temp2
        # La lista de los nums se actualizará para la siguiente vuelva
        nums[0] = nums[1]
        nums[1] = temp3
        nums[2] = nums[3]
        nums[3] = temp4
 
    return nums[0]
 
# -----------------------------------------------------------------------------------------------------------------------------------------------
# --> Vigénere Cipher ---------------------------------------------------------------------------------------------------------------------------
# @param code: Mensaje secreto que se debe revelar desencriptando la clave(code) que se dará
# @param key: Llave para obtener la clave de acceso (que se desencriptará)
# @return str: Mensaje con la llave y la clave de acceso.
def vigenere_cipher(code : str, key : str) -> str:
    # Analizar de primero los elementos que tiene el mensaje/codigo
    code_numbers = []
    for c in code:
        code_numbers.append(codification[c])

    # Obtener los números de la llave conforme vayan los elementos
    i = 0
    next = 0
    key_numbers = []
    while next != len(code_numbers):                
        key_numbers.append(codification[key[i]])
        i += 1
        i %= len(key)
        next += 1
    
    # Restar los valores de las listas entre sí para "desencriptar" el codigo encriptado con Vigenere cipher
    secret_string = []
    for i in range(len(code_numbers)):
        number_add = (int(code_numbers[i]) - int(key_numbers[i])) % 26        
        secret_string.append(codif_letters[number_add])    

    return f"Mensaje [{code}], Llave [{key}], Codigo Secreto: " + "".join(secret_string)

# -----------------------------------------------------------------------------------------------------------------------------------------------
# --> Principal----------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()