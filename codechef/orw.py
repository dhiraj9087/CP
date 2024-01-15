import math
import sys
input=sys.stdin.readline
def main():
    n,x,y=map(int,input().split())
    # a=x//3
    # b=x-a
    # print(a,b)
    if y // 3 > x:
        if n > x:
            print("NO")
        else:
            print("YES")
    else:
        z = x - y // 3
        if n - y // 3 - z // 2 <= 0:
            print("YES")
        else:
            print("NO")
    # ans = 0
    # # if y >= 3:
    # ans += min(x, y // 3)
    # x -= min(x, y // 3)
    # y //= 3
    # ans += x // 2
    # print("YES" if ans >= n else "NO")
    # if (x>=n and y>= 3*n) or x>=n//2:
    #     print("YES")
    #     return
    # if y>= 3*n and x>=n//2:
    #     print("YES")
    #     return
    # if x>=n//2:
    #     print("YES")
    #     return
    # print("NO")
for _ in range(int(input())):
   main()