F0 = 1
F1 = 1
for x in range(18): 
    if x%2==0:
        F0 = F0 + F1
        print(str(x)+":"+str(F0))
    else:
        F1 = F1 + F0
        print(str(x)+":"+str(F1))