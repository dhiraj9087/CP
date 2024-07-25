import math
import sys
input=sys.stdin.readline

def main():
    n,k=map(int,input().split())
    a=input().strip()
    s=list(a)
    for i in range(n):
        if k<=0:
            break
        if s[i]=='1' and k>0:
            s[i]='0'
            k-=1
    ind=[]
    for i in range(n):
        if s[i]=='1':
            ind.append(i)
    l=n-1
    ans=0
    while ind:
        front = ind.pop(0)
        tot = len(ind)
        ans += (l-front-tot)
    print(ans)
    # s2=list(a)
    # k2=k
    
    # left,right=0,0
    # if k%2==0:
    #     left=k//2
    #     right=k//2
    # else:
    #     left=k//2+1
    #     right=k//2


    
    # for i in range(n):
    #     if left<=0:
    #         break
    #     if s[i]=='1':
    #         s[i]='0'
    #         left-=1
    # for i in range(n):
    #     if right<=0:
    #         break
    #     if s[i]=='1':
    #         s[i]='0'
    #         right-=1
    
    # l=set()
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if int(s[i])>int(s[j]):
    #             l.add((i,j))
    # print(len(l))
    # ans=0
    # for i in range(n):
    #     if k<=0:
    #         break
    #     if s[i]=='1':
    #         s[i]='0'
    #         k-=1
    # print(s)
    # l=set()
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if int(s[i])>int(s[j]):
    #             l.add((i,j))
    
    # for i in range(n):
    #     if k2<=0:
    #         break
    #     if s2[i]=='1':
    #         s2[i]='0'
    #         k2-=1
    # # print(s)
    # l2=set()
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if int(s2[i])>int(s2[j]):
    #             l2.add((i,j))
    # print(min(len(l),len(l2)))

for _ in range(int(input())):
   main()