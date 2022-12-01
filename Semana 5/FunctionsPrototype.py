
def random(): #numeros pseudoaleatorios
    modulo = int(input("ingrese el modulo (m): "))
    multiplier = int(input("ingrese el multiplicador (a): "))
    increment = int(input("ingrese el incremento (c): "))
    seed = int(input("ingrese la semilla (s): "))
    num = int(input("ingrese la cantidad de numeros a generar (n): "))
    result = []
    predecesor = 0;
    for i in range(0,num):
        if i == 0:
            predecesor = (multiplier*seed + increment)%modulo
            result.append(predecesor)
        else:
            predecesor = (multiplier*predecesor + increment)%modulo
            result.append(predecesor)
    print("numeros pseudoaleatorios generados: ")
    print(result)
def hash():#funcion de dispersión
    liststring = input("Ingrese los elementos del arreglo, separado por comas. dentro de corchetes, ejemplo [a,b,c] \n")
    liststring = liststring.replace('[','')
    liststring = liststring.replace(']','')
    Array = liststring.split(',')
    module = int(input(f'Ingrese el modulo m, el cual debe de ser >= al largo del array ingresado , \n el cual es de {len(Array)} elementos:  \n'))
    output = ['_']*module #crear el array de salida de n tamaño al igual que el de entrada
    '''
    codigo encargado de hacer la función de dispoersión por cada elemento
    #en caso estar ocupado, buscar el espacio a la derecha más proximo disponible 
    (se asume que el array es continuo, es decir después del ultimo elemento le sige el primero)
    '''
    for entero in Array:
        index = (int(entero)%int(module)) #H(n) = n mod module
        if output[index] is not '_':
            while output[index] != '_':
                if(index >= len(Array)-1):
                    index = 0
                else:
                    index += 1
            output[index] = int(entero)
        else:
            output[index] = int(entero)

    #en caso el resultado del indice por la dispersión es mayor al tamaño del array existente
    #se aumenta el tamaño para satisfacer la función de dispersión
                
    print(f'Array original: {Array}')
    print(f'Array resultante: {output}')
option = int(input(''' 
1. Generar numeros pseudoaleatorios
2. Funcion de dispersión
      '''))
if option == 1:
    random()
elif option == 2:
    hash()