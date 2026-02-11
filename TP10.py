# programme classique :


a=0
b=1
while(a<b):
    a=int(input("a : ?"))
    b=int(input("b : ? "))
Adebut=a
Bdebut=b

continu=True
while(continu):
    d=a-b
    if(d>b):
        a=d
    if(d<a):
        a=b
        b=d
    if(a%d==0 and b%d==0):
        continu=False
print("Le PGCD de ",Adebut ," et ",Bdebut," est : ", d)



# sous forme de Fonction

def PGCD(a,b):
    if(a<b):
        return "Need a > b \n Exit"

    continu=True
    while(continu):
        d=a-b
        if(d>b):
            a=d
        if(d<a):
            a=b
            b=d
        if(a%d==0 and b%d==0):
            continu=False
            a=d
    return a


# print(PGCD(78,128))  // test pour voir si la condition a>b est bien respecté . 
print(PGCD(128,78))
