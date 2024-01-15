import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    add=sum(a)
    for i in range(n):
        if a[i]%2==0 and (add-a[i])%2==0:
            print("YES")
            return
        elif a[i]%2!=0 and (add-a[i])%2!=0:
            print("YES")
            return
    print("NO")




    
for _ in range(int(input())):
    main()