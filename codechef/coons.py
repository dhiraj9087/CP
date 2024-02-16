import math
import sys
input=sys.stdin.readline
def main():
    k,x,a=map(int,input().split())
    s,flag = 1,True
    for i in range(1, x):
        mini = s // (k - 1)
        while mini * (k - 1) <= s:
            mini += 1
        s += mini
        if s >= a:
            print("NO")
            flag = False
            return
    if k*(a-s)>a and flag:
        print("YES")
        return
    print("NO")
    
for _ in range(int(input())):
   main()