import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    ans=[]
    ind=0
    add=0
    while ind<len(a):
        if a[ind]>add:
            ans.append(a[ind])
            add+=a[ind]
            del a[ind]
        else:
           ind+=1
    print(n-len(ans))
    ans.extend(a)
    print(*ans)
for _ in range(int(input())):
   main()
    
