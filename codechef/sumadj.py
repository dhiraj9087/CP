import math
import sys
input=sys.stdin.readline
def cal(a):
    return sum(abs(a[i] - a[i-1]) for i in range(1, len(a)))
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    add = sum(abs(a[i] - a[i-1]) for i in range(1, len(a)))
    maxi=add
    for i in range(n):
            original = a[i]
            a[i] = 1
            new_sum = cal(a)
            maxi = max(maxi, new_sum)
            a[i] = k
            new_sum2 = cal(a)
            maxi = max(maxi, new_sum2)
            a[i] = original   
    print(maxi)
for _ in range(int(input())):
   main()