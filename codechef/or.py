import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ans=0
    c=0
    for i in range(n-k+1):
        flag=False
        for j in range(i,i+k):
            if a[j]%2!=0:
                flag=True
                break
        if flag:
            ans+=1
            
    print(ans)
        

        
    # print(ans)
for _ in range(int(input())):
   main()