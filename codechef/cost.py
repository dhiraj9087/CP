import math
import sys
input=sys.stdin.readline
def main():
    n = int(input())
    # ans = 0
    # while True:
    #     bins = bin(int(n))[2:].zfill(64)
    #     ind = bins.find("101")
    #     if ind == -1:
    #         break
    #     ones = bins[:ind].rstrip("0")
    #     maxi = len(ones) - 1
    #     n += 2 ** maxi
    #     ans += 2 ** maxi
    # print(int(ans))
    ans = 0
    while True:
        bins = bin(int(n))[2:].zfill(64)
        ind = bins.find("101")
        if ind == -1:
            break
        ones = 0
        lim = ind - 1
        for i in range(lim,-1,-1):
            if bins[i]=='1':
                ones+=1
        maxi = 0
        while (1 << (maxi + 1)) <= ones:
            maxi += 1
        n += (1 << maxi)
        ans += (1 << maxi)
    print(ans)

    # n=int(input())
    # b=bin(n)[2:]
    # ind=[]
    # for i in range(len(b)-1,-1,-1):
    #     a=b[i:3+i]
    #     if a=='101':
    #         ind.append(2+i)
    # num=0
    # num|=(1<<12)
    # num|=(1<<10)
    # num|=(1<<3)
    # num|=(1<<1)
    # print(b,ind,num)
    
for _ in range(int(input())):
   main()