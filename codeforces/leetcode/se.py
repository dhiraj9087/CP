import math
import sys
input=sys.stdin.readline
from collections import Counter
def main():
    k = 9
    x = 1
    # k = 7
    # x = 2
    num=1
    ans=0
    while True:
        bit=bin(num)[2:][::-1]
        for i in range(len(bit)):
            if (i+1)%x==0  and bit[i]=='1':
                # print(num) 
                ans+=1
        if ans>k:
            break
        num+=1
    # for i in range(10):
    #     bit=bin(i)[2:][::-1]
    #     for i in range(len(bit)):
    #         if (i+1)%2==0 and bit[i]=='1':
    #             print(bit)
    print(num-1)
# for _ in range(int(input())):
main()