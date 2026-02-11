"""from random import*
def L():
    L=[0]*8
    for i in range(0,8):
        return(L)
#programme principal
L=L()"""
#on fait appelle au sous programme pour générer la liste L
# et on fait le programme principal


#exercice1
#question1

def max(L):
    max=L[0]
    for i in range(8):
        if L[i]>max:
            max=L[i]
    return max

Liste=[5,4,7,12,1,7,9,3]
N=max(Liste)
print(N)

#question 2


def min(L):
    min=L[0]
    for i in range(8):
        if L[i]<min:
            min=L[i]
    return min

Liste=[5,4,7,12,1,7,9,3]
N=min(Liste)
print(N)

# question 3 et 4
L1=[5,4,7,12,8,7,9,3]
L2=[18,5,9,37,4,6,12]

def max(L):
    max=L[0]
    for i in range(8):
        if L[i]>max:
            max=L[i]
    return max

def min(L):
    min=L[0]
    for i in range(8):
        if L[i]<min:
            min=L[i]
    return min

def etend(L):
    return max(L)-min(L)

def compare(L1,L2):
    if etend(L1)>etend(L2):
        print("la liste 1 a une etendue plus  grande")
    else:
        print("la liste 2 a une etendue plus grande")
