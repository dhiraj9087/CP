import math
import sys
input=sys.stdin.readline
lcm=math.lcm
def main():
    n=int(input())
    # if n%3==0:
    #     print(1,n//3,n//3)
    #     return
    # if n%3==2:
    #     print(1,1,(n-1)//2)
    #     return
    # print(-1)
    # for j in range(1,100):
    #     for k in range(1,100):
    #         if lcm(1,j)+lcm(j,k)+lcm(k,1)==x:
    #             print(1,j,k)
    #             break
    #             return
    # print(lcm(2,44))
    if (n & (n - 1)) == 0:
        print(-1)
        return
    if n % 2 == 0:
        bit = 0
        while (1 << bit) & n == 0:
            bit += 1
        print(1 << bit, 1, (n - (1 << bit)) // 2)
        return
    print(1, 1, n // 2)
for _ in range(int(input())):
   main()