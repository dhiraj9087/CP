import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    skii=list(map(int,input().split()))
    mov=list(map(int,input().split()))
    bor=list(map(int,input().split()))
    a,b,c=[],[],[]
    for i in range(n):
        a.append([skii[i],i])
        b.append([mov[i],i])
        c.append([bor[i],i])
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)
    ans=0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if a[i][1]!=b[j][1] and a[i][1]!=c[k][1] and b[j][1]!=c[k][1]:
                    ans=max(ans,a[i][0]+b[j][0]+c[k][0])
    print(ans)
    # a=[]
    # for i in range(n):
    #     if max(skii[i],mov[i],bor[i])==skii[i]:
    #         a.append([skii[i],1])
    #     elif max(skii[i],mov[i],bor[i])==mov[i]:
    #         a.append([mov[i],2])
    #     else:
    #         a.append([bor[i],3])
    
    #     # a.append([max(skii[i],mov[i],bor[i]),i])
    # a.sort(reverse=True)
    # # print(a)
    # ans=0
    # c=0

    # flag1,flag2,flag3=False,False,False
    # ans+=a[0][0]
    # if a[0][1]==1:
    #     flag1=True
    # elif a[0][1]==2:
    #     flag2=True
    # else:
    #     flag3=True
    # for i in range(1,len(a)):
    #     if a[i][1]==1 and flag1==False:
    #         ans+=a[i][0]
    #         flag1=True
    #     if a[i][1]==2 and flag2==False:
    #         ans+=a[i][0]
    #         flag2=True
    #     if a[i][1]==3 and flag3==False:
    #         ans+=a[i][0]
    #         flag3=True
        
    # print(ans)
    # print(a)
    # ans=sum(a[:3])
    # print(ans)
for _ in range(int(input())):
   main()