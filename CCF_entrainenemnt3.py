from random import *

def mystere (n):
    rep = False 
    i = 0
    while (i<13):
        if (i*i == n):
            rep = True 
        i=i+1
    return rep 


def iniTab():
    tab = [0] * 6 
    for i in range (5):
        tab[i]= randint(0,9)
    return tab 

def sommeTab(Tab):
    somme = 0
    for i in range (5):
        somme =somme + Tab[i]
    return somme 

tab = iniTab()
somme = sommeTab(tab)
if (mystere(somme)== True):
    print(" c'est original ")
else :
    print("c'est pas original") 

def divTab(a):
    tab = []
    i= 1
    while (i<=a and len(tab)<10):
        if (a%i == 0):
            tab.append(i)
        i=i+1
    return tab

test = divTab(94)
print(test)