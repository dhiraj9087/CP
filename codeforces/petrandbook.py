n=int(input())
a=list(map(int,input().split()))
s=0
flag=0
while flag==0:
    for i in range(len(a)):
        s+=a[i]
        if s>=n:
            print(i+1,end=' ')
            flag=1
            break
        #print(s)
    if s<n:
        flag=0
