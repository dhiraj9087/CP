import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    v = list(map(int, input().split()))
    mp = {}
    for i in v:
        if i in mp:
            mp[i] += 1
        else:
            mp[i] = 1
    if len(mp) < 3:
        print(-1)
        return
    if 5 in mp or 7 in mp:
        print(-1)
        return
    if mp[1] > n - mp[1] or mp[1] < n // 3:
        print(-1)
        return
    if mp[2] < mp[4]:
        print(-1)
        return
    if (mp[2] + mp[3]) != (mp[4] + mp[6]):
        print(-1)
        return
    while mp[2]:
        if mp[4] == 0:
            break
        print(1, 2, 4)
        mp[4] -= 1
        mp[2] -= 1
    while mp[2]:
        if mp[6] == 0:
            break
        print(1, 2, 6)
        mp[6] -= 1
        mp[2] -= 1
    while mp[3]:
        if mp[6] == 0:
            break
        print(1, 3, 6)
        mp[6] -= 1
        mp[3] -= 1

solve()