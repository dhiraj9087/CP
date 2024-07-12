import math
import sys
input=sys.stdin.readline
def ispowerof2(n):
    return n != 0 and (n & (n - 1)) == 0
def main():
    n=int(input())
    a=list(map(int,input().split()))
    vari = [0] * 32
    arr = a[:]
    for i in arr:
        cnt = 0
        while i > 0:
            if i & 1:
                vari[cnt] = 1
            cnt += 1
            i = i >> 1
    s = 0
    for i in vari:
        if i == 0:
            break
        s += 1

    ans = 0
    cmp = (1 << s)
    for i in a:
        if i >= cmp:
            ans += 1

    print(ans)
    # o=1
    # a.sort()
    # for i in range(n):
    #     o = o|a[i]
    #     print(o,end=' ')
    # print()
    # o=1
    # for i in range(n-1,-1,-1):
    #     o = o|a[i]
    #     print(o,end=' ')
    # print()
    # ans=[]
    # for i in range(n):
    #     num = o&a[i]
    #     if ispowerof2(num+1)==True:
    #         ans.append(a[i])
    # print(23&1)
for _ in range(int(input())):
   main()