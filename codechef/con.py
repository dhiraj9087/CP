# import math
# import sys
# input=sys.stdin.readline
# def main():
#     n=int(input())
#     a=list(map(int,input().split()))
#     a.sort()
#     ans=[]
#     even,odd=[],[]
#     for i in range(1,n,2):
#         even.append(a[i])
#     for i in range(0,n,2):
#         odd.append(a[i])
#     ans=even+odd
#     print(*ans)
#     for i in range(1,len(ans)-1):
#         if not ((ans[i-1]<ans[i]>ans[i+1]) or (ans[i-1]>ans[i]<ans[i+1])):
#             print(-1)
#             return
#     print(*ans)    
# for _ in range(int(input())):
#    main()
import math
import sys
input=sys.stdin.readline
def verify(ans):
    for i in range(1,len(ans)-1):
        if ((ans[i-1]<ans[i]>ans[i+1]) or (ans[i-1]>ans[i]<ans[i+1])):
            continue
        return False
    return True
def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    b=[0]*n
    c=[0]*n
    ind=0
    for i in range(n):
        if ind>=n:
            ind=1
        b[ind]=a[i]
        ind+=2
    ind=1
    for i in range(n):
        if ind>=n:
            ind=0
        c[ind]=a[i]
        ind+=2
    ans=[-1]
    if verify(b):
        ans=b
    elif verify(c):
        ans=c
    print(*ans)
for _ in range(int(input())):
   main()