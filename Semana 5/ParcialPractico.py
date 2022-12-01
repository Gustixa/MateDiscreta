#Diego Andres Alonzo Medinilla 20172
from sympy import Range

# ________________Numeros binarios
unumber = "111111111111111111111111111111111111"
num1 =    "000000000000000000000000000000000000"
num2 =    "000000000000000000000000000000000000"
counter = 0
# Listas a usar
universe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
con1 = []
con2 = []
cdif = []
cint = []
cun = []
ccom = []
# Ingreso de datos
while (True):
    a = input("Ingrese un valor alfanumerico\n")
    con1.append(a)
    exit = input("Desea Salir?y/n\n")
    if (exit=='y'):
        break
while (True):
    a = input("Ingrese un valor alfanumerico\n")
    con2.append(a)
    exit = input("Desea Salir?y/n\n")
    if (exit=='y'):
        break
# Generacion de binarios
for x in con1:
    chainl= list(num1)
    chainl[universe.index(x)]="1"
    num1 = "".join(chainl)
for y in con2:
    chainl= list(num2)
    chainl[universe.index(y)]="1"
    num2 = "".join(chainl)

for k in range(36):
    if (int(num1[k])*int(num2[k]))==1:
        cint.append(universe[k])
    if (int(num1[k])*int(num2[k]))==0 and num1[k]=="1":
        cdif.append(universe[k])        
    if (int(num1[k])+int(num2[k]))==1:
        cun.append(universe[k])
    elif (int(num1[k])+int(num2[k]))==2:
        cun.append(universe[k])
    if (int(num1[k])+int(unumber[k]))==1:
        ccom.append(universe[k])

print("INTERSECCION: " + str(cint))
print("UNION: " + str(cun))
print("COMPLEMENTO: " + str(ccom))
print("DIFERENCIA: " + str(cdif))
print(con1)
print(con2)

# ________________Funcion de dispersion

m = int(input("Ingrese un entero no negativo (modulo): "))
a = int(input("Ingrese un entero no negativo (multiplicador): "))
c = int(input("Ingrese un entero no negativo (incremento): "))
s = int(input("Ingrese un entero no negativo (semilla): "))
n = int(input("Ingrese la cantidad de numeros aleatorios a generar, debe ser mayor o igual que 1: "))
b = []
b.append((s*a+c)*m)

for x in Range(n):
    b.append((b[x-1]*a+c)*m)
print("La lista con el metodo pseudoaleatorio de numeros es: " + str(b))

