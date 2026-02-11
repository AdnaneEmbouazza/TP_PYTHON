def complementaire (K):
    if K=="A":
        K="T"
    if K=="T":
        K="A"
    if K=="G":
        K="C"
    if K=="C":
        K="C"

    return K

def mystere(brin1 , brin2):
    if len(brin1) != len(brin2):
        B= False
    else:
        B= True
        for i in range(len(brin1))-1:
            if brin1[i]!=complementaire(brin2[i]):
                B=False
    return B


def plusFrequent(brin1):
    compteA=0
    compteC=0
    compteT=0
    compteG=0

    for i in range (len(brin1)):
        if brin1[i]=="A":
            compteA=compteA+1
        if brin1[i]=="T":
            compteT=compteT+1
        if brin1[i]=="C":
            compteC=compteC+1
        if brin1[i]=="G":
            compteG=compteG+1

    if compteG > compteC and compteG > compteA and compteG > compteT:
        return "le caractère le plus présent dans la chaine est G"
    if compteC > compteG and compteC > compteA and compteC > compteT:
        return "le caractère le plus présent dans la chaine est C"
    if compteA > compteC and compteA > compteG and compteA > compteT:
        return "le caractère le plus présent dans la chaine est A"
    if compteT > compteC and compteT > compteA and compteT > compteG:
        return "le caractère le plus présent dans la chaine est T"


