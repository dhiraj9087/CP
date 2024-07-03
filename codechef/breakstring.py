import math
import sys
input=sys.stdin.readline
def main():
    a=input().strip()
    b=input().strip()
    if len(a+b)==len(set(a+b)):
        print(len(a)+len(b))
        return
    c=0
    for i in b:
        if i in a:
            c+=1
    print(len(a)+len(b)-c)
for _ in range(int(input())):
   main()