# Escriba un programa de computadora escrito en Python que realice lo que se indica
#
# Dados 2 conjuntos A y B (suponga el conjunto universo U formado por 26 letras)
# minusculas y 10 dígitos decimales), realizar las operaciones COMPLEMENTO, UNIÓN,
# INTERSECCIÓN y DIFERENCIA. Determinar si un elemento específico está o no en un cojunto.

# Entrada: A y B conjuntos
# Salida: El resultado de la opaeración elegida por el usuario.
# Alumno: Samuel Argueta - 211024
# Matemática discreta

def main():
    '''Metodo de ejecución del programa.'''
    setUniverse = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                   'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    setA = input(
        "\nIngrese n cantidad de valores entre la a-z y 1-10, pueden ser mixtos, no solo letras o solo numeros: ")
    setB = input("\nNuevamente, ingrese n cantidad de valores entre la a-z y 1-10, pero esta vez, no deben ser los mismos valores de antes, pero no se descarta la posibilidad" +
                 "los valores pueden ser mixtos, no solo letras o solo numeros: ")

    # Limpieza de datos
    setA = [value for value in setA if value != ',']
    setB = [value for value in setB if value != ',']
    selection = menu()
    if(selection == 1):
        union(setA, setB, setUniverse)
    elif(selection == 2):
        intersection(setA, setB, setUniverse)
    elif(selection == 3):
        diference(setA, setB, setUniverse)
    elif(selection == 4):
        complement(setA, setB, setUniverse)
    else:
        searchElement(setA,setB)


def menu() -> int:
    ''' The menu where shows all the options available to the
    user'''
    next_step = False
    print("1. Union")
    print("2. Interseccion")
    print("3. Diferencia")
    print("4. Complemento")
    print("5. Buscar elemento")
    print("6. Salir")
    selection = int(input("Ingrese una de las opciones disponibles: "))
    return selection


def union(setA: str, setB: str, setUniverse: str):
    ''' union -> void
        Creating a set with the union operation.
        @ setA: str, first set of data entered by the user.
        @ setB: str, second set of data entered by the user.
        @ setUniverse: str, this is where all the comparisons begin, between the
         data entered in the previous sets.
    '''
    setEntered(setA, setB)
    mask = [setUniverse.index(value) for value in setA]
    for value in setB:
        if setUniverse.index(value) not in mask:
            mask.append(setUniverse.index(value))
    union = [setUniverse[value] for value in mask]
    print("The union of the set is: ")
    print(union)


def intersection(setA: str, setB: str, setUniverse: str):
    ''' intersection -> void
        Creating a set with the interesction operation.
        @ setA: str, first set of data entered by the user.
        @ setB: str, second set of data entered by the user.
        @ setUniverse: str, this is where all the comparisons begin, between the
         data entered in the previous sets.
    '''
    mask1 = [setUniverse.index(value) for value in setA]
    intersection, mask2 = [], []
    setEntered(setA, setB)
    for value in setB:
        if setUniverse.index(value) in mask1:
            mask2.append(setUniverse.index(value))
    intersection = [setUniverse[value] for value in mask2]
    print("The intersection intersection of the set is: ")
    print(intersection)

    # Verifying if both sets share elements


def complement(setA: str, setB: str, setUniverse: str):
    ''' complent -> void
        Creating a set with the complement operation.
        @ setA: str, first set of data entered by the user.
        @ setB: str, second set of data entered by the user.
        @ setUniverse: str, this is where all the comparisons begin, between the
         data entered in the previous sets.
    '''
    complementOfA, complementOfB = [], []
    setEntered(setA, setB)
    for value in setUniverse:
        if (value not in setA):
            complementOfA.append(value)
        if (value not in setB):
            complementOfB.append(value)

    print("The complement of the set A is: ")
    print(complementOfA)
    print("The complement of the set B is: ")
    print(complementOfB)


def diference(setA, setB, setUniverse):
    ''' diference -> void
        Creating a set with the difference operation.
        @ setA: str, first set of data entered by the user.
        @ setB: str, second set of data entered by the user.
        @ setUniverse: str, this is where all the comparisons begin, between the
         data entered in the previous sets.
    '''
    diferenceAToB, diferenceBToA = [], []
    setEntered(setA, setB)
    for value in setA:
        if (value not in setB):
            diferenceAToB.append(value)
    for value in setB:
        if (value not in setA):
            diferenceBToA.append(value)

    print("The diference between A to B is: ")
    print(diferenceAToB)
    print("The diference between B to A is:")
    print(diferenceBToA)


def setEntered(setA: str, setB: str):
    '''setEntered -> void
        This shows at the user the sets, entered by him, before de operation.
        @ setA: str, first set of data entered by the user.
        @ setB: str, second set of data entered by the user.
    '''
    print("Conjunto ingresado A:")
    print(setA)
    print("Conjunto ingresado B:")
    print(setB)

def searchElement(setA:str, setB: str):
    '''searchElement -> void
        This search an specific element that the user wants.
        @ setA: str, the first set inputed by the user.
        @ setB: str, the secont set inputed by the user.
    '''
    selection = menuSets();
    element = input("Ingrese el elemento que desea encontrar: ")
    if(selection == 1):
        if(element in setA):
            print("El elemento pertenece al conjuto")
        else:
            print("El elemento que desea buscar, no se encuentra en tal conjunto")
    else:
        if(element in setB):
            print("El elemento pertenece al conjuto")
        else:
            print("El elemento que desea buscar, no se encuentra en tal conjunto")

def menuSets()->int:
    ''' menuSet -> int
        This method it's used to select the specific set inputed by the user
        then, he can search an specific element by the set selected.
        @return selection: int, set selected
    '''
    print("1. Conjunto A")
    print("2. Conjunto B")
    selection = int(input("Ingrese el conjunto al cual desea encontrar un elemento: "))
    return selection


    
if __name__ == "__main__":
    main()
