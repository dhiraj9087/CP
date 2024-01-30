import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    gcd=math.gcd
    if k==1:
        print(1)
        return
    if n==k:
        print(*list(range(1,n+1)))
        return
    a=n//k
    ans=a
    arr=[]
    for i in range(k):
        arr.append(ans)
        ans+=a
    print(*arr)
    # print(math.gcd(2,4))
for _ in range(int(input())):
   main()