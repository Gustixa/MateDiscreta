'''
Arturo Argueta
modulo con operaciones matriciales
'''

'''
Param: Recibe una lista de ayacencia
Return: Matriz de adyacencia
'''
import numpy

from numpy.linalg import matrix_power
def matrixConverter(AdyList):
    values = []
    #obtener los valores que hay en la lista
    for relations in AdyList:
        for element in relations:
            if element not in values:
                values.append(element)
    values.sort()
    matrix = []
    for i in range(len(values)):
        matrix.append(["0"]*len(values))
        if i < len(AdyList):
            for j in AdyList[i]:
                matrix[i][values.index(j)] = "1"
    return matrix
def matrixConverteru(AdyList , universe):
    matrix = []
    for i in range(len(universe)):
        matrix.append(["0"]*len(universe))
        if i < len(AdyList):
            for j in AdyList[i]:
                matrix[i][universe.index(j.replace(" ", ""))] = "1"
    return matrix
#booleano donde indica si es o no reflexiva una matriz
def isReflexive(matrix): 
    for a in range(len(matrix)):
        A = matrix[a][a]
        if  A != "1":
            return 0
    return 1           

#recibe una matriz, devuelve su transpuesta
def TMatrix(matrix):
    TM = []*len(matrix)
    for i in range(len(matrix)):
        TM.append(["0"]*len(matrix))
        
    #iterar de modo A(ij) -> T(ji) 
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            TM[j][i] = matrix[i][j] 
    return TM
#matriz identidad In
def identity(N):
    I = []
    for i in range(N):
        I.append(["0"]*N)
    for a in range(N):
        I[a][a] = "1"
    return I
#indica si es simétrica
def isSimetric(matrix):
    TM = TMatrix(matrix)
    for row in range(len(matrix)):
        if "".join(matrix[row]) != "".join(TM[row]):
            return 0
    return 1
#antisimetría
def isAntiSimetric(matrix):
    TM = TMatrix(matrix)
    I = identity(len(matrix))
    R = []
    #calcular el producto
    for i in range(len(matrix)):
        r = []
        for a in range(len(matrix)):
            p = str(int(matrix[i][a])*int(TM[i][a]))
            r.append(p)
        R.append(r)
    # verificar si hay presendencia (lo opuesto: R > I)
    for i  in (range(len(matrix))):
        if int("".join(R[i])) > int("".join(I[i])):
            return 0
    return 1
#convertirlo a numerico
def toInteger(matrix):
    M = []
    for i in range(len(matrix)):
        M.append(["0"]*len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            M[i][j] = int(matrix[i][j])
    return M
        
#indica si es transitiva
def isTransitive(matrix):
    M = numpy.matrix(toInteger(matrix), dtype=bool)
    R = M*M
    R = R.astype(int)
    R = R.tolist()
   
    for i  in (range(len(matrix))):
        if int("".join(str(x) for x in R[i])) > int("".join(matrix[i])): #calcular la procedencia
            return 0
    return 1
def composition(R,S):
    R = numpy.matrix(toInteger(R), dtype=bool)
    S = numpy.matrix(toInteger(S), dtype=bool)
    Result = R*S
    Result = Result.astype(int)
    Result = Result.tolist()
    return Result

def setUniverse(R,S):
    universe = []
    for relations in R:
        for element in R:
            if element not in values:
                universe.append(element)
    for relations in S:
        for element in S:
            if element not in values:
                universe.append(element)
    universe = universe.sort()
    return universe

def setAristList(compose, universe):
    AristList = []
    for i in range(len(universe)):
        for j in range(len(universe)):
            if compose[i][j] == 1:
                AristList.append(f'[{universe[i]},{universe[j]}]')
    return f'[{"".join(AristList)}]'
            
#  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
# | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
# | |      __      | || |  _______     | || |  _________   | || | _____  _____ | || |  _______     | || |     ____     | |
# | |     /  \     | || | |_   __ \    | || | |  _   _  |  | || ||_   _||_   _|| || | |_   __ \    | || |   .'    `.   | |
# | |    / /\ \    | || |   | |__) |   | || | |_/ | | \_|  | || |  | |    | |  | || |   | |__) |   | || |  /  .--.  \  | |
# | |   / ____ \   | || |   |  __ /    | || |     | |      | || |  | '    ' |  | || |   |  __ /    | || |  | |    | |  | |
# | | _/ /    \ \_ | || |  _| |  \ \_  | || |    _| |_     | || |   \ `--' /   | || |  _| |  \ \_  | || |  \  `--'  /  | |
# | ||____|  |____|| || | |____| |___| | || |   |_____|    | || |    `.__.'    | || | |____| |___| | || |   `.____.'   | |
# | |              | || |              | || |              | || |              | || |              | || |              | |
# | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
#  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
#  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.                     
# | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |                    
# | |    _____     | || |     __       | || |   _______    | || |    _____     | || |   _______    | |                    
# | |   / ___ `.   | || |    /  |      | || |  |  _____|   | || |   / ___ `.   | || |  |  ___  |   | |                    
# | |  |_/___) |   | || |    `| |      | || |  | |____     | || |  |_/___) |   | || |  |_/  / /    | |                    
# | |   .'____.'   | || |     | |      | || |  '_.____''.  | || |   .'____.'   | || |      / /     | |                    
# | |  / /____     | || |    _| |_     | || |  | \____) |  | || |  / /____     | || |     / /      | |                    
# | |  |_______|   | || |   |_____|    | || |   \______.'  | || |  |_______|   | || |    /_/       | |                    
# | |              | || |              | || |              | || |              | || |              | |                    
# | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |                    
#  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'                   



