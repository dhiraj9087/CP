import math
import sys
input=sys.stdin.readline
def main():
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    arr=[]
    c,l=0,0
    for i in a:
        if i>=x:
            c+=1
            l += i-x
        else:
            arr.append(i)
    arr.sort(reverse=True)
    for i in arr:
        if l >= x-i:
            l -= x-i
            c+=1
        else:
            break
    print(c)
    
for _ in range(int(input())):
   main()