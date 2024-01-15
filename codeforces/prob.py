from collections import Counter
import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    d=Counter(s)
    ans=0

    for key, value in d.items():
        ind = ord(key) - ord('A') + 1
        if ind <= value:
            ans += 1

    print(ans)
    # print(ord('A')-ord())
    # for i in r/ange(n):
        
    # print(d)
for _ in range(int(input())):
   main()