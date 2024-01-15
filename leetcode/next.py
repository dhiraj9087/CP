import math
import sys
input=sys.stdin.readline
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in a:
        if i>0 and a[k-1]<=i:
            ans+=1
    print(ans)
# for _ in range(int(input())):
main()