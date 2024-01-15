import math
import sys
input=sys.stdin.readline


def main():
    n, m = map(int, input().split())
    a = [input() for _ in range(n)]
    s,k = "vika",0
    for i in range(m):
        for j in range(n):
            if k<4 and a[j][i] == s[k]:
                k += 1
                break
    if k==4:
        print("YES")
    else:
        print("NO")
for _ in range(int(input())):
    main()