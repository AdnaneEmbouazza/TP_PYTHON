def min(L1,L2):
    L3=[]
    for i in range(0,len(L1)):
        if(L1[i]>=L2[i]):
            L3.append(L2[i])
        else:
            L3.append(L1[i])
    return L3

def decprem(n):
    P=[2,3,5,7,11,13]
    exp=[0,0,0,0,0,0,0]
    for i in range(0,8):
        cnt=0
        while(n%P[i]==0 and n!=1):
            cnt+=1
            n=n//P[i]
        exp[i]=cnt

n1=decprem(78)
n2=decprem(128)
n3=min(n1,n2)
for i in range(0,8):
