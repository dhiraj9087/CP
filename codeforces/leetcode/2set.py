import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    add=sum(range(1,n+1))
    if add%2!=0:
        print("NO")
        return
    tar=add//2
    a,b=set(),set()
    for i in range(n,0,-1):
        if i<=tar:
            a.add(i)
            tar=tar-i
        else:
            b.add(i)
    print("YES")
    print(len(a))
    print(*a)
    print(len(b))
    print(*b)
    # print(a,b)
# for _ in range(int(input())):
main()