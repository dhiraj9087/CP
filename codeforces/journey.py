import math
import sys
input=sys.stdin.readline
def main():
    n,a,b,c=map(int,input().split())
    add=a+b+c
    # if add>=n:
    #     if a>=n:
    #         print(1)
    #         return
    #     if a+b>=n:
    #         print(2)
    #         return
    #     print(3)
    mini = n//add
    if n%add==0:
        print(mini*3)
        return
    if n%add<=a:
        print((mini*3)  + 1)
        return
    if n%add<=a+b:
        print((mini*3 )+ 2)
        return
    print((mini*3) + 3)
    
for _ in range(int(input())):
   main()