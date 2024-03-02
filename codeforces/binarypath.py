import math
import sys
input=sys.stdin.readline
def main():
    n = int(input())
    a = input().strip()
    b = input().strip()
    d = {}
    for i in range(n):
        var = a[:i+1] + b[i:]
        d[var] = d.get(var, 0) + 1
    ans1 = min(d.keys())
    ans2 = d[ans1]
    print(ans1)
    print(ans2)
for _ in range(int(input())):
   main()
