def solve():
    n = int(input())
    c=0
    for i in range(n):
        x,y,z = map(int,input().split())
        if x+y+z >= 2:
            c += 1
 
    print(c)


solve()
