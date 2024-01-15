import math
def solve(a,b):
    # r=b-a
    # for _ in range(r):
    #     if b%a==0:
    #         print(a)
    #         return 'YES'
    #     else:
    #         a+=1
    # return 'NO'
    return math.gcd(a,b)


for _ in range((int(input()))):
    a,b=map(int,input().split())
    print(solve(a,b))
