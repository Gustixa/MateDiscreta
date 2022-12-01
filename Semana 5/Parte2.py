'''
Ejercicio numero 2 para el parcial 1 de matematica discreta
Alumno: Josúe Samuel Argueta Herández - 211024
'''

def main():
    '''main -> void
        This method it's the main thread, where all the program start
    '''   
    selection = menu()
    if(selection == 1):
        print("------------")
        print("PSEUDORANDOM")
        print("------------")
        linearCongruentialMethod()
    else:
        print("------------")
        print("FUNCION DE DISPERSION HASH")
        print("------------")
        hash()    
    
 
def menu() -> int:
    ''' menu -> int
        This methods it's use to show of at the user
        the available options for the system.
        @ return selection:int, options selected from the user
    '''
    print("1. Linear Congruential (pseudorandom Numbers)")
    print("2. function dispersion (Hash)")
    selection = int(input("Ingrese una de las opciones: "))
    return selection

def linearCongruentialMethod():
    ''' linearCongruentialMethod -> void
        Creating the random numbers
    '''
    seed = int(input("Ingese la el valor de la semilla: "))
     
    # Modulus parameter
    module = int(input("Ingrese el parametro del modulo: "))
     
    # Multiplier term
    multiplier = int(input("Ingrese el termino multiplicador: "))
     
    # Increment term
    increment = int(input("Ingrese el termino de incremento: "))
 
    # Number of Random numbers
    # to be generated
    noOfRandomNums = int(input("Ingrese el numero de numeros aleatorios que desea obtener: "))
 
    # To store random numbers
    randomNums = [0] * (noOfRandomNums)
    # Initialize the seed state
    randomNums[0] = seed
 
    # Traverse to generate required
    # numbers of random numbers
    for i in range(1, noOfRandomNums):
        # Follow the linear congruential method
        randomNums[i] = ((randomNums[i - 1] * multiplier) +
                                         increment) % module

    # Print the generated random numbers
    for i in randomNums:
        print(i, end = " ")
    
 
def hash():
    '''hash->void
    Dispersion function, this simulate a data structure hash, where try to put 
    a value in a location indicates, but, if there's no space to that location
    try to do like a linkedList, where the value follow to the previous value.
    '''
    array = input("Ingrese los elementos del arreglo, separado por comas. dentro de corchetes, ejemplo a,b,c \n")
    array = array.split(',')
    module = int(input(f'Ingrese el modulo m, el cual debe de ser >= al largo del array ingresado , \n el cual es de {len(array)} elementos:  \n'))
    output = ['_']*module #crear el array de salida de n tamaño al igual que el de entrada

    for value in array:
        index = (int(value)%int(module)) #H(n) = n mod module
        if output[index] != '_':
            while output[index] != '_':
                if(index >= len(array)-1):
                    index = 0
                else:
                    index += 1
            output[index] = value
        else:
            output[index] = value

                
    print(f"Arreglo original: {array}")
    print(f"Arreglo resultante: {output}")


'''
    Here is where we indicate what methods we want to run.
'''
if __name__ == '__main__':
    main()