# algo A1

# n=int(input(" Combien de places de concert souhaitez vous acheter ?"))
# prix= n * 20
# if n>=3 :
# prix=prix*0.9
# print (prix)

#Rep = input("Etes vous Etudiant ?")
#n = int(input("nbre de places ?"))
#prix = n * 20
#if Rep == "oui":
    #prix = prix * 0.75
#print(prix)

Rep=input("Etes vous Etudiant ?")
n=int(input("nbre de places ?"))
m=input("quel mois somme nous ?")
if m=="juin":
    prix= n * 16
else :
    prix= n* 20
    if Rep == "oui" :
        prix=prix * 0.75
    elif n>=3 and m!="juin":(
    prix)=prix*0.9
print (prix)
