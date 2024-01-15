import math
import sys
input=sys.stdin.readline
def main():
    n = int(input())
    s = input().strip()[::-1]
    cnt = 0
    v = []
    for i in range(n):
        if s[i] == '0':
            v.append(i - cnt)
            cnt += 1
    
    size = len(v)
    for i in range(1, size):
        v[i] = v[i] + v[i - 1]

    for i in v:
        print(i, end=' ')
    
    for i in range(n - cnt):
        print(-1, end=' ')
    
    print()
for _ in range(int(input())):
   main()