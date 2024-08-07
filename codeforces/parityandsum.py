import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    odd,even=[],[]
    for i in a:
        if i%2==1:
            odd.append(i)
        else:
            even.append(i)
    if len(odd)==0 or len(even)==0:
        print(0)
        return
    even.sort()
    maxi=max(odd)
    ans=len(even)
    for i in even:
        if i<maxi:
            maxi+=i
        else:
            ans+=1
            break

    print(ans)
for _ in range(int(input())):
   main()