import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    ans = "IDK"
    for i in range(n - 1):
        if s[i] == '0':
            ans = "NO"
        print(ans)
    if ans == "IDK" and s[n - 1] == '1':
        ans = "YES"
    else:
        ans = "NO"
    
    print(ans)
for _ in range(int(input())):
   main()