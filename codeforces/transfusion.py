import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    s1,s2,n1,n2=0,0,0,0
    for i in range(n):
        if i%2==0:
            s1+=a[i]
            n1+=1
        else:
            s2+=a[i]
            n2+=1
    if n1 > 0 and n2 > 0 and s1 % n1 == 0 and s2 % n2 == 0 and (s1 // n1) == (s2 // n2):
        print("YES")
        return
    print("NO")

for _ in range(int(input())):
   main()