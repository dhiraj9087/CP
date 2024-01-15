import math
import sys
input=sys.stdin.readline
def main():
    n,a,q=map(int,input().split())
    s=input()
    add=a
    add2=0
    if n==a:
        print("YES")
        return
    for i in s:
        if i=='+':
            add+=1
            add2+=1
        elif i=='-': 
            add-=1

        if add==n:
            print("YES")
            return
    # if n==a:
    #     print("YES")
    #     return
    # if add==n:
    #     print("YES")
    #     return
    if add2>=(n-a):
        print("MAYBE")
        return
    print("NO")
    # print(add,sub)
    
for _ in range(int(input())):
   main()