import math
import sys
input=sys.stdin.readline
lim=2**30
def main():
    a,b=map(int,input().split())
    ans=0
    d=abs(a^ans-b^ans)
    for i in range(31):
        m=1<<i
        ans|=m
        diff=abs(a^ans-b^ans)
        if diff<d:
            d=diff
        else:
            ans^=m
    print(ans)


    # l,r=0,lim-1
    # mini=float('inf')
    # while l<=r:
    #     mid=l+(r-l)//2
    #     if abs((a^mid)-(b^mid))<mini:
    #         mini=abs((a^mid)-(b^mid))
    #     elif abs((a^mid)-(b^mid)
    # X = 0
    # for i in range(29, -1, -1):
    #     bit_A = (a >> i) & 1
    #     bit_B = (b >> i) & 1

    #     if bit_A != bit_B:
    #         X |= (1 << i)

    # print(X)
    
for _ in range(int(input())):
   main()