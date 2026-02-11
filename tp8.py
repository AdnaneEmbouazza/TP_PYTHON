#TP8 Listes

#I) Listes :
    #1)definition

#liste =[]
#for i in range(0,9):
    #liste=liste+[i+1]
#print(liste)

#2) Initialisation d'une liste :
    #a)

#dim=int(input("saisir la dimension de la liste"))
#L=dim*[0]
#for i in range(0,dim):
    #L[i]=int(input("saisir une valeur"))
#print(L)

    #b)
#n=int(input("saisir la dimension de la liste"))
#L=[]
#for i in range(0,n):
    #L.append(int(input()))
#print(L)

#3) exercices :
# dim=10

# dim=10
# somme=0
# L=dim*[0]
# from random import*

# for i in range(0,10):
#     L[i]=randint(1,6)
#     somme=somme+L[i]
# print(somme)

#ou bien

#somme=0
#L=[]
#from random import*

#for i in range(0,10):
    #L.append(randint(1,6))
    #somme=somme+L[i]
#print(somme)


#exercice 2

# dim=int(input("saisir la taille"))
# L=dim*[int(input("saisir les valeurs"))]
# M=L[0]
# n=len(L)
# for i in range(0,n-1):
#     if L[i]>M:
#         M=L[i]
# print(M)


#II) Commandes principales :

# L1=[1,3,5,7,9]
# L2=[0,2,4,6,8]
# L=L1+L2
# L.append(9)
# print(L)


#Exercice 3

# dim=10
# somme=0
# L=dim*[0]
# from random import*

# for i in range(0,10):
#     L[i]=randint(1,6)
#     if L[i]%2==0:
#         somme=somme+1
#     else:
#         somme=somme-2
        
# for i in range(1,10):
#         if L[i]==L[i-1]:
#         somme=somme+5
# if somme>10:
#     somme=somme+3
# print(L)
# print(somme)


n=int(input(""))

for i in range (n):
    tab[i]=int(input("saisir une valeur i"))

aux=tab[0]

for j in range (n-1):
    if tab[i]> tab[i+1]:
        aux=tab[i]
        tab[i]=tab[i+1]
        tab[i+1]=aux

for i in range (n):
    print(tab[i])