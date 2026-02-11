#I)Opérations sur les chaines de caractère :

#1)commandes de base

#mot1="bonjour,"
#mot2=input("écris ton prenom")
#phrase=mot1+mot2
#print(phrase)#concaténation des deux chaines
#print(len(phrase))#donne la longueur de la chaine
#print(phrase[0],phrase[7])#extrait deux éléments de la chaine
#print(phrase[5:8])#extrait une partie de la chaine
#print(phrase[6:])#extrait la phrase à partird'un certain rang
#print(phrase[:7])#extrait la phrase jusqu'à un certain rang
#modif=phrase[:8]+"maman"#moifie une phrase
#print(modif)


#2)quelque test
# voir TP

#II)exemple de programme

#1)

#phrase=input("écris une phrase sans ponctuation")
#l=len(phrase)
#c=1
#for i in range(0,l):
    #if phrase[i]==" ":
        #c=c+1
#print(c)
#print(l)


#quel est le role de ce programme
#le programme sert à compter le nombre de caractères + le nombre de  mots

#que teste l'instruction : if phrase[i]==" ":
    #elle teste le présence d'espace au sein de la chaine de caractère

#2)

#mot=input("ecris un mot")
#l=len(mot)
#nouveaumot=" "#au debut il n'y a rien dans le nouveau mot
#if l%2==0:
    #for i in range(0,l-1,2):
        #nouveaumot=nouveaumot+mot[i]+mot[i+1]+"#"
#else:
    #for i in range(0,l-1,2):
        #nouveaumot=nouveaumot+mot[i]+mot[i+1]+"#"+mot[i+2]="#"
        #nouveaumot=nouveaumot+mot[l-1]
#print(nouveaumot)

#3)

# n=int(input("saisir un entier"))
# binaire=""
# q=n
# while q//2!=0:
#     q=
#     binaire=str(q%2)+binaire #la commande str transformeun nbre en une chaine de caractère 
# print(binaire)

#III) EXERCICES 

#exercice1
#ecrire un programme qui demande une phrase et qui affiche cette phrase écrite à l'envers 

# phrase=input("saisir la phrase \n")
# l=len(phrase)
# phrase2=""
# for i in range(1,l+1):
#     lettre=phrase[l-i]
#     phrase2=phrase2+lettre
# print(phrase2)


