import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    start=0
    while start<n and a[start]==0:
        start+=1
    end = len(a)-1
    while end>0 and a[end]==0:
        end-=1
    a=a[start:end+1]
    # w=a.strip("0 ")
    zero=a.count(0)
    # print(a,zero)
    if len(a)==0:
        print(0)
        return
    if zero>0:
        print(2)
        return
    print(1)
    # if n==1:
    #     if a[0]==0:
    #         print(0)
    #         return
    #     print(1)
    #     return
    # if min(a)>0:
    #     print(1)
    #     return
    # if len(set(a))==1 and a[0]==0:
    #     print(0)
    #     return
    # if min(a)==0:
    #     if (a[0]==0 and a[-1]!=0) and (0 in a[1:-1]):
    #         print(2)
    #         return
    #     if (a[0]!=0 and a[-1]==0) and (0 in a[1:-1]):
    #         print(2)
    #         return
    #     if (a[0]==0 and (0 not in a[1:])) or (a[-1]==0 and (0 not in a[:-1])):
    #         print(1)
    #         return
        
    #     if (a[0]==0 or a[-1]==0) and (0 in a[1:-1]):
    #         print(2)
    #         return
    #     if (a[0]==0 or a[-1]==0) and (0 not in a[1:-1]):
    #         print(1)
    #         return
        
    #     print(2)
    #     return
    # print(2)
              
for _ in range(int(input())):
   main()