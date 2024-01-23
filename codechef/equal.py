import math
import sys
input=sys.stdin.readline
def main():
    x,y=map(int,input().split())
    if x==y:
        print(0)
        return
    if abs(x-y)==1:
        print(1)
        return
    ind=abs(x-y)
    ind1=int((2 * ind)**0.5)
    ind2=ind1*(ind1+1)//2
    while ind2 < ind or (ind2-ind) % 2 != 0 :
        ind1+=1
        ind2+=ind1
    print(ind1)

    # a=x+y
    # if a%2==1:
    #     print(a//2 + 1)
    #     return
    # print(a//2 - 1)
    # i=1
    # ans=0
    # if x<y:
    #     while x<y:
    #         if i%2==0:
    #             if x-i == y or y-(x-i) == i+1:
    #                 ans+=1
    #                 x-=i
    #             else:
    #                 ans+=1
    #                 y-=i
    #         else:
    #             if x+i==y or y-(x+i) == i+1:
    #                 ans+=1
    #                 x+=i
    #             else:
    #                 ans+=1
    #                 y+=i
    #         i+=1
    #     print(ans)
    #     return
    # while x>y:
    #     if i%2==0:
    #         if y-i == x or x-(y-i) == i+1:
    #             ans+=1
    #             y-=i
    #         else:
    #             ans+=1
    #             x-=i
    #     else:
    #         if y+i==x or x-(y+i) == i+1:
    #             ans+=1
    #             y+=i
    #         else:
    #             ans+=1
    #             x+=i
    #     i+=1
    
    # print(ans)
for _ in range(int(input())):
   main()