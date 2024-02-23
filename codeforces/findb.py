import math
import sys
input=sys.stdin.readline
def main():
    n, q = map(int, input().split())
    c = list(map(int, input().split()))
    prifix = [0] * (n + 1)
    prifix1 = [0] * (n + 1)
    for i in range(1, n + 1):
        prifix[i] = prifix[i - 1] + c[i - 1]
        prifix1[i] = prifix1[i - 1] + (1 if c[i - 1] == 1 else 0)
    for _ in range(q):
        l, r = map(int, input().split())
        s1 = prifix[r] - prifix[l - 1]
        s2 = prifix1[r] - prifix1[l - 1]
        if l == r or s2 > s1 - (r - l + 1):
            print("NO")
        else:
            print("YES")
for _ in range(int(input())):
   main()


