import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    l=[]
    d2=[0]*32
    for i in range(n):
        a,b=map(int,input().split())
        if a==1:
            d2[b]+=1
        else:
            bit=0
            flag=True
            d=d2[:]
            while bit < 30:
                if (b >> bit) & 1:
                    if d[bit] <= 0:
                        flag=False
                    else:
                        d[bit] -= 1
                d[bit + 1] += d[bit] // 2
                bit += 1
            if flag:
                print("YES")
            else:
                print("NO")
        # l.append([a,b])
    # print(l)
    # d2={i:0 for i in range(32)}
    # # d2=[0]*32
    # for i,j in l:
    #     if i==1:
    #         d2[j]+=1
    # # bit=0
    # for i,j in l:
    #     if i==2:
    #         flag=True
    #         d=d2.copy()
    #         bit=0
    #         while bit<30:
    #             if (j>>bit) & 1:
    #                 if d[bit]>0:
    #                     d[bit]-=1
    #                 else:
    #                     flag=False
    #             d[bit+1] = d[bit+1] + (d[bit]//2)
    #             bit+=1
    #         if flag:
    #             print("YES")
    #         else:
    #             print("NO")
    # print(d)
# for _ in range(int(input())):
main()