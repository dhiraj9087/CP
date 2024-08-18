import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    for k in range(m):
        s=input().strip()
        if len(s)!=n:
            print("NO")
            continue
        d1={}
        d2={}
        ans = "YES"
        for i in range(n):
            char = s[i]
            num=a[i]
            if char in d1 and d1[char]!=num:
                ans="NO"
                break
            if num in d2 and d2[num]!=char:
                ans = "NO"
                break
            d1[char]=num
            d2[num]=char
        print(ans)

             

for _ in range(int(input())):
   main()