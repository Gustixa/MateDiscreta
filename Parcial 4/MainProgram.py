#Programa Principal
'''
Arturo Argueta
Programa Principal
'''
from MatrixOperator import *
import ast
opt = -1
while opt != 3:
    opt = int(input('''
1. Propiedades de Lista de Adyacencia de Relacion
2. Composicion de relaciones
3. Salir
'''))
    if opt == 1:
        
        sub = int(input('''
1. conjunto universo en la lista de ayacencia --> A = '{' [universe] , ...... }
2. sin conunto universo en la lista de ayacencia
'''))
        if sub in [1, 2]:
            AdyList = str(input('''
Ingrese la lista de ayacencia
el formato es: elementos de la relación separados por comas (,)
y encerrar elementos en corchetes, ejemplo: [a,b,c]
relaciones separadas por comas (,)   
y encerrar todo el conjunto entre corchetes
ejemplo: [[a,b,c],[c,f]]                     
'''))
            AdyList = AdyList.replace(' ', '')
            strs = AdyList.replace('[','').split('],') 
            lists = [map(str, s.replace(']','').split(',')) for s in strs]  
            AdyList = []
            matrix = []
            for m in lists:
                AdyList.append(list(m))
            if sub == 1:
                universe = AdyList.pop(0)
                matrix = matrixConverteru(AdyList, universe)
                
            if sub == 2:
                matrix = matrixConverter(AdyList)
            else:
                sub == -1
            print("matriz de adyacencia: ")
            for row in matrix:
                print (f'| {" ".join(row)} |')
            P = [0,0,0,0]
            P[0] = isReflexive(matrix)
            P[1] = isSimetric(matrix)
            P[2] = isAntiSimetric(matrix)
            P[3] = isTransitive(matrix)
            print(f'''
propiedades:
[𝑝𝑅,𝑝𝑆,𝑝𝐴,𝑝𝑇]
{P}
            ''')
    elif opt == 2:
        universe = str(input('ingrese el conjunto universo: \n'))
        s = str(input('Ingrese la lista de ayacencia S: \n'))
        r = str(input('Ingrese la lista de adyacencia R: \n'))
        universe = universe.replace(' ', '')
        universe = universe.replace('{', '')
        universe = universe.replace('}', '')
        universe = universe.split(',')
        
        strs = s.replace('[','').split('],') 
        lists = [map(str, p.replace(']','').split(',')) for p in strs]
        
        strs2 = r.replace('[','').split('],') 
        lists2 = [map(str, p.replace(']','').split(',')) for p in strs2]
        s = []
        r = []
        for m in lists:
                s.append(list(m))
        for m in lists2:
                r.append(list(m))   
        s = matrixConverteru(s,universe)
        r = matrixConverteru(r,universe)
        
        SR = composition(s,r)
        RS = composition(r,s)

        print(f'R°S : {setAristList(SR,universe)}')
        print(f'S°R : {setAristList(RS,universe)}')


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
            
            
   
