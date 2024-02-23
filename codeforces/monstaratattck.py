import math
import sys
input=sys.stdin.readline
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))
    diff = [0] * (n + 1)
    for i in range(n):
        diff[abs(x[i])] += a[i]
    rng = k
    for i in range(1, n + 1):
        if rng < diff[i]:
            print("NO")
            return
        rng -= diff[i]
        rng += k
    print("YES")
for _ in range(int(input())):
   main()