import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=input().strip()
    b=input().strip()
    s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans=[0]*n
    # ans = []
    for i in range(n):
        ind = ord(b[i]) - ord(a[i])
        while ind % 3 != 0 or ind < 0:
            ind += 26
        ans[i]=(ind//3)
        # ans.append(ind // 3)
    print(*ans)

    
for _ in range(int(input())):
   main()