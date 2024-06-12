import math
import sys
input=sys.stdin.readline
def main():
    n,m=map(int,input().split())
    a=[]
    for i in range(n):
        s=input().strip()
        a.append(s)
    # print(a)
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')
    
    for i in range(n):
        for j in range(m):
            if a[i][j] == '#':
                min_x = min(min_x, i)
                max_x = max(max_x, i)
                min_y = min(min_y, j)
                max_y = max(max_y, j)
    center_x = (min_x + max_x) // 2
    center_y = (min_y + max_y) // 2
    print(center_x+1,center_y+1)
for _ in range(int(input())):
   main()