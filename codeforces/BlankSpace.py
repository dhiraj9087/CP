for i in range((int(input()))):
    n=int(input())
    a=list(map(int,input().split()))
    count0=0
    maxlen=0
    for i in range(n):
        if a[i]==0:
            count0+=1
        else:
            if count0>maxlen:
                maxlen=count0
            count0=0
    if count0>maxlen:
        maxlen=count0
    print(maxlen)
