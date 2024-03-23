import math
import sys
input=sys.stdin.readline
def main():
    n = int(input())
    a = list(map(int, input().split()))
    last = a[-1]
    ans = 'YES'
    for i in range(n - 2, -1, -1):
        if a[i] <= last:
            last = a[i]
            continue
        b, c = divmod(a[i], 10)
        if b <= c <= last:
            last = b
            continue
        else:
            ans = 'NO'
            break
    print(ans)
 
for _ in range(int(input())):
   main()