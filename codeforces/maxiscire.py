import math
import sys
input=sys.stdin.readline

def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    pair=[]
    for i in range(n):
        if i==n-1:
            arr=a[:n-1]
        elif i==0:
            arr=a[i+1:]
        else:
            arr=a[0:i]+a[i+1:]
        arr.sort()
        l=((len(arr)+1) // 2 )-1
        print(arr,l)

        s=set()
        ele=0
        for j in range(len(arr)):
            s.add(arr[j])
            if len(s)==l+1:
                ele=arr[j]
                break

        
        # first,second=0,0
        # first=arr[0]
        # for j in range(len(arr)):
        #     if arr[j]!=first:
        #         second=arr[j]
        #         break
        second = arr[((len(arr)+1) // 2 )-1] 
        pair.append([a[i],ele])
    print(pair)
    ans=0
    d={}
    for i in range(n):
        if b[i]==1:
            d[a[i]]=1
        else:
            d[a[i]]=0
    print(d)
    cmp=b.count(1)
    if cmp%2==0:rem=k//cmp
    else:rem=k//cmp

    for i in range(len(pair)):
        if d[pair[i][0]]==1 or d[pair[i][1]]==1:
            ans=max(ans,pair[i][0]+pair[i][1]+k)
    print(ans)
    pair.sort(key=lambda x:x[0])
    print(pair)  

for _ in range(int(input())):
   main()