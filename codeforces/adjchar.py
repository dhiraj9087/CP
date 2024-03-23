import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    if n%2==1:
        print("NO")
        return
    print("YES")
    ans=""
    for i in range(n//2):
        ans+=(chr(65+i))
        ans+=(chr(65+i))
    print(ans)
for _ in range(int(input())):
   main()