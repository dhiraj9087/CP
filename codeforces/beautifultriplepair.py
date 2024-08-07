import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    d = {}
    ans = 0
    for i in range(n - 2):
        triplet = (a[i], a[i + 1], a[i + 2])
        mist = [0] * 3
        mist[0] = (0, a[i + 1], a[i + 2])
        mist[1] = (a[i], 0, a[i + 2])
        mist[2] = (a[i], a[i + 1], 0)
        for trip in mist:
            ans += d.get(trip, 0) - d.get(triplet, 0)
            d[trip] = d.get(trip, 0) + 1
        d[triplet] = d.get(triplet, 0) + 1
    print(ans)
for _ in range(int(input())):
   main()