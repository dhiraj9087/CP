def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    s1,s2=0,0
    maxs1,maxs2=0,0
    for i in range(n):
        if a[i]!=0:
            s1+=1
        maxs1=max(maxs1,s1)
        if a[i]==0:
            maxs1=max(maxs1,s1)
            s1=0
    for i in range(n):
        if b[i]!=0:
            s2+=1
        maxs2=max(maxs2,s2)
        if b[i]==0:
            maxs2=max(maxs2,s2)
            s2=0
    # print(maxs1,maxs2)
    if maxs2>maxs1:print("Addy")
    elif maxs1>maxs2:print("Om")
    else:print("Draw")
    
for _ in range(int(input())):
    main()