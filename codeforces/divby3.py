import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    add=sum(a)
    if sum(a)%3==0:
        print(0)
        return
    mod=add%3
    if mod==2:
        print(1)
        return
    for i in a:
        if i%3==1:
            print(1)
            return
    print(2)
    # print(mod)
for _ in range(int(input())):
   main()