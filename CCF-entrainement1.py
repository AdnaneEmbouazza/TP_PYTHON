from random import *

#algo de la question 3
# variables 
def somme(m):
    somme = 0
    for i in range (len(m)):
        somme = somme + m[i]
    return somme 

m = [0,0,0,0,0,0,0,0,0,0,0]
for j in range (100):
    j = randint (0,10)
    m[j] = m[j] + 1

print(m)

#algo de la question 1,2

#Variables 
def somme(m):
    somme = 0
    for i in range (len(m)):
        somme = somme + m[i]
    return somme 

m = [0,0,0,0,0,0,0,0,0,0,0]
result = 0
n = 0
while(result != 11):
    j = randint (0,10)
    m[j]=1
    n = n+1 
    result = somme(m)

print(n)


