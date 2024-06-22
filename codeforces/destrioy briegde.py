import math
import sys
input=sys.stdin.readline
def main():
    n,c = map(int,input().split())
    a = list(map(int,input().split()))
    mul=[0]*n
    mul[0]=1
    cal = 0
    # for i in range(n):
    #     if mul[i] == 0:
    #         continue
    #     for j in range(n):
    #         if mul[j] == 0:
    #             cal += a[i] * a[j]
    
    if cal<=c:
        print(1)
        return
    ind = 1
    while ind < n:
        multi = -1
        for i in range(n):
            if mul[i] == 0 and (multi == -1 or a[i] > a[multi]):
                multi = i
        mul[multi] = 1
        ind += 1
        cal = 0
        for i in range(n):
            if mul[i] == 0:
                continue
            for j in range(n):
                if mul[j] == 0:
                    cal += a[i] * a[j]
        if cal<=c:
            print(ind)
            return
for _ in range(int(input())):
   main()