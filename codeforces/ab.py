import math
import sys
input=sys.stdin.readline
def main():
    n,a,b=map(int,input().split())
    if a==b:
        if a>=n:
            print("Alice")
            return
        if (n-a-1)%(b+1)==0:
            print("Bob")
            return
        print("Alice")
        return
        # if n%2==0:
        #     print("Bob")
        #     return
        # print("Alice")
        # return
    if a>b:
        print("Alice")
        return
    # if n<=a:
    #     print("Alice")
    #     return
    if b>a:
        if a>=n:
            print("Alice")
            return
        print("Bob")
        return
    # if b>a and b>=n:
    #     print("Bob")
    #     return
    # if b>a and a>=n:
    #     print("Alice")
    

    print("Bob")
for _ in range(int(input())):
   main()