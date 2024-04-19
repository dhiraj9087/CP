import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=input().strip()
    ans=[]
    prev=0
    for i in range(0,n,2):
        if a[i]!=a[i+1]:
            if prev==0:
                if a[i]=='0':
                    ans.append(i+2)
                    prev=1
                else:
                    ans.append(i+1)
                    prev=1
            else:
                if a[i]=='1':
                    ans.append(i+2)
                    prev=0
                else:
                    ans.append(i+1)
                    prev=0
    print(len(ans))
    print(*ans)
for _ in range(int(input())):
   main()

   