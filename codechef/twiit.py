N,K=map(int,input().split())
P=[]
for i in range(K):
    
    S=input()
    if(S=='CLOSEALL'):
        P=[]
        print(len(P),"1",P)
    elif S in P:
        P.remove(S)
        print(len(P),"2",P)
    else:
        P.append(S)
        print(len(P),"3",P)
        