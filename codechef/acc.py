import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    s=input().strip()
    if s[0]=='0':
        print("NO")
        return
    val=0
    for i in range(n):
        if s[i]=='0':
            if val<=0:
                print("NO")
                return
            val-=1
        elif s[i]=='1':
            val=k
        # if s[i]=='1':
        #     val+=k
        # else:
        #     val-=1
    # print(val)
    print("YES" if val>=0 else "NO")
for _ in range(int(input())):
   main()