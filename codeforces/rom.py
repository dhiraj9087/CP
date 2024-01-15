import math
import sys
input=sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    flag=False
    d = {}
    d[0] = True
    maxi = 0
    for i in range(n):
        if i % 2 == 0:
            maxi += a[i]
        else:
            maxi -= a[i]
        if maxi in d:
            flag=True
        else:
            d[maxi] = True
    if flag:
        print("YES")
        return
    print("NO")
for _ in range(int(input())):
   main()

   # print(v)
    # s = SortedList()
    # s.add(v[0][1])
    # print(s)
    # ans = 0

    # for i in range(1, n):
    #     ans += i - s.bisect_left(v[i][1])
    #     s.add(v[i][1])

    # print(ans)