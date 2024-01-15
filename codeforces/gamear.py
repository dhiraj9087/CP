import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    # print(a)
    arr=[]
    ans=a[0]
    # for i in range(n-1):
    #     arr.append([(a[i+1],a[i]),a[i+1]-a[i]])
    # arr.sort(key=lambda x:x[1])
    for i in range(n-1):
        ans=min(ans,a[i+1]-a[i])
    # print(arr)
    if k==1:
        print(ans)
        return
    if k==2:
        # s=(arr[0][1])
        # ans=s
        # for i in range(n):
        #     ans=min(ans,abs(s-a[i]))
        # print(ans)
        # return
        for i in range(n):
            for j in range(i):
                ele=a[i]-a[j]
                s=next((ind for ind,val in enumerate(a) if val>=ele),n)
                if s<n:
                    ans=min(ans,a[s]-ele)
                if s>0:
                    ans=min(ans,ele-a[s-1])
        print(ans)
        return
    print(0)
    # if k%2==1:
    #     for i in range(len(arr)-1):
    #         if (arr[i][1]==arr[i+1][1] or (arr[i+1][1]%arr[i][1]==0)):
    #             print(0)
    #             return
    #     print(1)   
    #     # print(arr[0][1]-arr[1][1])
    #     return
    # for i in range(len(arr)-1):
    #     if (arr[i][1]==arr[i+1][1] or (arr[i+1][1]%arr[i][1]==0)):
    #         print(0)
    #         return
    # print(1) 
    # print(abs(arr[0][1]-min(a)))
for _ in range(int(input())):
   main()