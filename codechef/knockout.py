import math
import sys
input=sys.stdin.readline
def main():
    a=list(map(int,input().split()))
    n=len(a)
    # a.sort(reverse=True)
    # print(a)
    cnt=[]
    for i in range(n):
        c=0
        for j in range(n):
            if i!=j and a[i]>a[j]:
                c+=1
        cnt.append(c)
    ans=[]
    for i in range(n):
        if cnt[i]<=14 and cnt[i]>=7:
            ans.append(3)
        elif cnt[i]<=6 and cnt[i]>=3:
            ans.append(2)
        elif cnt[i]<=2 and cnt[i]>=1:
            ans.append(1)
        elif cnt[i]>14:
            ans.append(4)
        else:
            ans.append(0)
    print(*ans)
for _ in range(int(input())):
   main()