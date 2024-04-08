import math
import sys
input=sys.stdin.readline
def main():
    n = int(input())
    a = []
    for _ in range(n):
        q=int(input())
        a.append(q)
    print(a)
    n=len(a)
    l,r,ans,mini,maxi=0,0,0,float('inf'),float('-inf')
    while r < n:
        if r < len(a):
            mini = min(mini, a[r])  
            maxi = max(maxi, a[r]) 
            if (maxi - mini) <= 2:  
                ans += (r - l + 1)  
            else:
                while (maxi - mini)> 2:  
                    l += 1
                    mini = min(a[l:r+1])
                    maxi = max(a[l:r+1])
                    if (maxi - mini) <= 2:
                        ans += (r - l + 1)
                        break
        r += 1  
    print(ans)
# for _ in range(int(input())):
main()