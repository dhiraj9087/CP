import math
import sys
input=sys.stdin.readline
def main():
    n=input()
    a,b=n[0],n[1]
    arr=['a','b','c','d','e','f','g','h']
    for i in range(1,9):
        if str(i)!=b:
            print(a+str(i))
    for i in range(8):
        if arr[i]!=a:
            print(str(arr[i])+b)
for _ in range(int(input())):
   main()