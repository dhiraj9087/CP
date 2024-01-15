
import math
import sys
input=sys.stdin.readline
def main():
    n = int(input())
    size = n * (n - 1) // 2
    v = list(map(int, input().split()))
    maximum = max(v)
    mp = {}
    for i in v:
        mp[i] = mp.get(i, 0) + 1
    maxi = n - 1
    ans = [10000000000] * n
    for j in mp.items():
        cnt = j[1]
        while cnt:
            less = min(maxi, cnt)
            while ans[less] != 10000000000:
                less -= 1
            ans[less] = j[0]
            cnt -= less
    final = len(ans)
    ans.reverse()
    for ind in range(final):
        if ans[ind] == 10000000000:
            ans[ind] = maximum
    for k in ans:
        print(k, end=" ")
    print()





    
for _ in range(int(input())):
    main()