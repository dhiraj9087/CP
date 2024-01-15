for i in range((int(input()))):
    N=int(input())
    Q=list(map(int,input().split()))
    W=list(map(int,input().split()))
    for i in range(N):
        if Q[i]<W[i]:
            Q[i],W[i]=W[i],Q[i]
    if Q[N-1]==max(Q) and W[N-1]==max(W):
        print("Yes")
    else:
        print("No")
