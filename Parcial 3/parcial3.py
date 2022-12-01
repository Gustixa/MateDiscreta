'''
    Criptografía. Parcial práctica 3, Matemática Discreta
    Josúe Samuel Argueta Hernández -- 211024
'''
codificationValues = {
    "A" : "00", "B" : "01", "C" : "02", "D" : "03", "E" : "04", "F" : "05", "G" : "06", "H" : "07", "I" : "08", "J" : "09", "K" : "10", "L" : "11",
    "M" : "12", "N" : "13", "O" : "14", "P" : "15", "Q" : "16", "R" : "17", "S" : "18", "T" : "19", "U" : "20", "V" : "21", "W" : "22", "X" : "23",
    "Y" : "24", "Z" : "25", "0" : "26", "1" : "27", "2" : "28", "3" : "29", "4" : "30", "5" : "31", "6" : "32", "7" : "33", "8" : "34", "9" : "35",
}

def main():
    ''' main -> void
        This is the main thread where all the program begin.
    '''
    print("Iniciando...")
    selection = 0
    while(selection != 3):
        selection = menu()
        if(selection == 1):
            message = input("Ingrese el mensaje a encriptar, ejemplo, Hola: ").upper()
            #p, q = verifyInput_PQ()
            n = int(input("n = ")) # p * q
            e = int(input("e =")) # junto con n, son la llave publica
            encrypt(message, n,e)
        elif(selection ==2):
            messageCodified = input("Ingrese el mensaje encriptado, ejemplo: 1191 1906 2497 0709 = ")
            p, q = verifyInput_PQ()
            e = int(input("e = "))
            decrypt(messageCodified,p,q,e)
        elif(selection == 3):
            code = input("ingrese el codigo secreto: ")
            key = input("Ingrese la llave: ").upper()
            vigenere_cipher(code, key)
        else:
            print("Apagando...")

def menu():
    ''' menu -> int
        This method helps to show the options availables to the user, and if the option selected
        it is available, and of course, if the input is numeric
        @ return selection: int, option selected from the user.
    '''
    selection = 0
    next_step = False
    while(next_step == False):
        print("1. Encriptacion RSA")
        print("2. Desencriptacion RSA")
        print("3. Vigener cipher")
        print("4. Salir")
        try:
            selection = int(input("Ingrese una de las opciones: "))
            if(selection < 1 or selection > 4):
                print("Debe ingresar una opcion valida")
            else:
                next_step = True
        except ValueError:
            print("Debe ingresar un valor numerico")
    return selection

def encrypt(m, n, e):
    ''' encrypt -> void
        Encrypting a message, using the word, and primes values.
    '''
    #n = p * q
    m = m.upper()
    # Encode the secret message
    blocks = []
    element = ""
    i = 1
    for c in m:
        if c != " ":
            element += str(codificationValues[c])
            if i % 2 == 0:
                blocks.append(int(element))
                element = ""
            i += 1

    # Show block elements
    message_encrypted = []
    for b in blocks:
        part_encrypted = pow(b, e) % n
        message_encrypted.append(str(part_encrypted)) if len(str(part_encrypted)) == 4 else message_encrypted.append("0" + str(part_encrypted))
    print(f"+ {m} : " + " ".join(message_encrypted))

def decrypt(c,p,q,e):
    ''' decrypt -> void
        This method is use to desencrypt the message, using the message encrypted and prime values
    '''
    delta = (p - 1) * (q - 1)
    n = p * q
    c = c.split(" ")
    
    # Get private key
    key = euclid_extended(e, delta)
    
    # Using algorithm of module exponentiation
    the_chars_key = list(codificationValues.keys())
    the_numbers_value = list(codificationValues.values())
    letters = []
    for i in c:
        see = pow(int(i), key) % n

        # If a letter with the value of one number (one unit)
        if len(str(see)) != 4:
            see = "0" + str(see)
            if len(str(see)) != 4: # If the case end with letter A
                see = "0" + str(see)
                
        # Getting the letters founded to reveal the message encrypted
        see = str(see)
        letter1 = see[0] + see[1]
        letter2 = see[2] + see[3]

        # Concatenate the letters showed
        letters.append(the_chars_key[the_numbers_value.index(letter1)])
        letters.append(the_chars_key[the_numbers_value.index(letter2)])
    print(f"- C {c} ; Llave privada [{key}], mensaje desencriptado: " + "".join(letters))

def euclid_extended(a : int, b : int):
    ''' euclid_extended -> int
        This helps to find the private key using the euclid algorithm
    '''
    nums = [1, 0, 0, 1]
    while b != 0: # While b not equal to "b", iterate
        # Searching
        temp1 = a // b
        temp2 = a - b * temp1
        temp3 = nums[0] - temp1 * nums[1]
        temp4 = nums[2] - temp1 * nums[3]
        # Updating a and b values
        a = b
        b = temp2
        # The list of the nums will be updated to the next come back
        nums[0] = nums[1]
        nums[1] = temp3
        nums[2] = nums[3]
        nums[3] = temp4
 
    return nums[0]

def vigenere_cipher(code : str, key : str):
    ''' vigenere_cipher -> void
        This is useful to know the key value to send the work in canvas.
    '''
    codif_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    # Analyze the elements of the message/code
    code_numbers = []
    for c in code:
        code_numbers.append(codificationValues[c])

    # Get the numbers of the key for each element
    i = 0
    next = 0
    key_numbers = []
    while next != len(code_numbers):                
        key_numbers.append(codificationValues[key[i]])
        i += 1
        i %= len(key)
        next += 1
    
    # Substract the values of the lists to decrypt the code encrypted with Vigener cipher
    secret_string = []
    for i in range(len(code_numbers)):
        number_add = (int(code_numbers[i]) - int(key_numbers[i])) % 26        
        secret_string.append(codif_letters[number_add])    

    print(f"Mensaje [{code}], Llave [{key}], Codigo Secreto: " + "".join(secret_string))


def primeVerification(n):
    ''' primeVerification -> boolean
        This method verify if the number requested is useful for the program
        If it's not prime number or the input, return false.
        @ return booelan, it represents a right or bad input
    '''
    c = 0
    x = 2
    if(n>=2):
        while(x <=n/2):
            if(n%x == 0):
                c += 1
                x += 1
            else:
                x += 1
        if(c==0):
            return True
        else:
            return False
    else:
        return False

def verifyInput_PQ():
    ''' verifyInput -> int
        This method is a complementation fo primeVerification, because
        receives the input from the user, and in base of the result from primeVerification
        can repeat again and again the same input.
        @return p: int, a prime number, q:int, a prime number
    '''
    p = int(input("Ingrese un numero primpo, p = "))
    while primeVerification(p) == False:
        print("Debe ingresar un numero primo!!!")
        p = int(input("Ingrese un numero primpo, p = "))
    
    q = int(input("Ingrese un numero primno, q = "))
    while primeVerification(q) == False or p == q:
        print("Ingrese un numero primo, este tambien debe ser diferente de p!!!")
        q = int(input("Ingrese un numero primno, q = "))
    values = [p,q]
    return values
    

if __name__ == "__main__":
    main()
