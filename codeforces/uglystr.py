import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    if 'map' not in s and 'pie' not in s:
        print(0)
        return
    i=2
    ans=0
    while i<n:
        temp = s[i-2:i+1]
        if temp=='map' or temp=='pie':
            ans+=1
            i+=3
        else:
            i+=1
    print(ans)
for _ in range(int(input())):
   main()