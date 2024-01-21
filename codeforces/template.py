import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=input().strip()
    b=input().strip()
    c=input().strip()
    if a==c or b==c:
        print("NO")
        return
    if n==1 and a!=b:
        print("YES")
        return
    for i in range(n):
        if (a[i]==b[i] and a[i]!=c[i]) or (a[i]!=b[i] and b[i]!=c[i] and c[i]!=a[i]):
            print("YES")
            return
    print("NO")   
for _ in range(int(input())):
   main()
