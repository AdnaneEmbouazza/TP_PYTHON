from random import *

def rangement(tab):
    n = len(tab)-1
    i = 0
    while(i < n):
        i = i + 1
        j = i
        while(j!=0 and tab[j-1]>tab[j]):
            sauv = tab[j]
            tab[j]=tab[j-1]
            tab[j-1] = sauv
            j = j-1
    return tab

def ecc (tab):
    n = len(tab)
    ajout= tab[0]
    i = 1
    while (i < n):
        ajout = ajout + tab[i]
        tab[i]= ajout
        i = i + 1
    return tab

def tabmultiple5():
    tab = 6 * [0]
    for i in range(6):
        n = randint(4 , 10)
        tab[i] = 5*n
    return tab








