import math
def solve():
    n=int(input())
    a=list(map(int,input().split()))
    q=[]
    for i in range(n):
        q.append(abs(i+1-a[i]))
    return math.gcd(*q)
for _ in range((int(input()))):
    print(solve())
