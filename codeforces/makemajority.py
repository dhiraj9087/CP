import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    l=[]
    flag=False
    for i in s:
        if i=='0':
            if flag==False:
                l.append('0')
                flag=True
        else:
            l.append('1')
            flag=False
    zero,one=l.count('0'),l.count('1')
    if one>zero:
        print("Yes")
        return
    print("No")

for _ in range(int(input())):
   main()