import math
import sys
input=sys.stdin.readline
def main():
    x,y,n=map(int,input().split())
    a=[x]
    while len(a)!=n and x<=y:
      x+=1
      a.append(x)
    print(a)
for _ in range(int(input())):
   main()


    # x, y, n = map(int, input().split())
    # a = [y]
    
    # for i in range(1, n):
    #     a.append(a[-1] - i)
    
    # if a[-1] < x:
    #     print(-1)
    # else:
    #     a[-1] = x
    #     print(*a[::-1])