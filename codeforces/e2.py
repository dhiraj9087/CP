import math
import sys
input=sys.stdin.readline

def psti(s, i, str):
    return s[:i] + str + s[i:]
    
def pstj(s, j, str):
    return s[:j + 1] + str + s[j + 1:]
    
def solve():
    n = int(input())
    s = input().strip()
    v = []
    i = 0
    j = n - 1
    cnt = 0
    flag = True
    if n % 2:
        print(-1)
        return
    while i < j:
        if s[i] != s[n - i - 1]:
            i += 1
            j -= 1
        else:
            if s[i] == '0':
                s = pstj(s, j, s[i])
                v.append(j + 1)
            else:
                s = psti(s, i, s[i])
                v.append(i)
            i += 1
            j += 1
            n += 2
            cnt += 1

        if cnt > 300:
            flag = False
            break
    if not flag:
        print(-1)
        return
    print(cnt)
    for i in v:
        print(i, end=' ')
    print()
for _ in range(int(input())):
   solve()
