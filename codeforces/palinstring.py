import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input()
    one,zero=0,0
    for i in s:
        if i=='0':
            zero+=1
    a,b=0,0
    # print(zero,one)
    if zero%2==0 or zero==1:
        print("BOB")
        return
    print("ALICE")
    # print(s[::-1])
    
for _ in range(int(input())):
   main()