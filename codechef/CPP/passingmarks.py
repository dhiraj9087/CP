# cook your dish here
for i in range((int(input()))):
    n,x=map(int,input().split())
    lst=list(map(int,input().split()))
    lst.sort()
    if(n==x):
        print(min(lst)-1)
    elif(x==1):
        print(max(lst)-1)
    else:
        print(lst[n-x]-1)

