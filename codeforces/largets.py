import math
import sys
input=sys.stdin.readline
def main():
    s=input().strip()
    for i in range(1,len(s)):
        a=s[:i]
        b=s[i:]
        # print(a,b)
        if (a[0]!='0' and b[0]!='0') and int(b)>int(a):
            print(a,b)
            return
    print(-1)
for _ in range(int(input())):
   main()