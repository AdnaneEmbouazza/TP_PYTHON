'''
#affichage de nombre
n=int(input("saisir un nbre entier "))
for i in range (1,n+1) :
    print(i)
print ("ce sont les nbres entiers inférieurs à n ?")

'''

'''
#affichage de nbre
n=int(input("saisir un nbre entier "))
for i in range (1,n+1,2) :
    print(i)
print ("ce sont les nbres impairs inférieurs à n ")

'''

'''
#conversion décimal vers binaire
a=int(input("saisir un nbre entier inférieur à 255"))
for i in range (1 , 8+1) :
    print(a%2)
    a=a//2
print(" l'octet correspondant est cette série de bits lue à l'envers ")

'''
'''
#pile ou face
c = -5
from random import *
for i in range (1 , 8+1) :
    n=randint (0,1)
    if n==1 :
        c= c+1
print("le capital final est " , c,"euros")

'''

'''
#somme entiers
s=0
for i in range (1 , 50+1) :
    s = s+ i
print ("la sommes des nbres entiers entre 50 et 1 est de " , s)

'''