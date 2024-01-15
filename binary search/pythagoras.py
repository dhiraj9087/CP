n=int(input())
c=0
# for i in range(1,n):
#     # print(i)
#     if i*i + (i+1)*(i+1)==(i+2)*(i+2):
#         c+=1
#         print(i)
# print(c)
import math

def solve():
    counT = 0
    # n = int(input())
    for i in range(1, n+1):
        for j in range(i, n+1):
            lhs = i*i + j*j
            rhs = int(math.sqrt(lhs))
            if rhs**2 == lhs and rhs <= n:
                counT += 1
                print(lhs,rhs)

    print(counT)

solve()

