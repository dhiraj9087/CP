import math
import sys
input=sys.stdin.readline
def fun(a,tar):
    s = set()
    for num in a:
        ele = tar - num
        if ele in s:
            return True
        s.add(num)
    return False
def main():
    n,x,z=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    if z%x==0:
        print(z//x)
        return
    ind=z//x
    # print(ind)
    ans=x*(ind+1)
    tar=ans-z
    # print(ans,tar)
    flag=fun(a,tar)
    if flag:
        print(ind+1)
        return
    print(-1)
    # s = set()
    # flag=False
    # for i in a:
    #     # add += num
    #     if (tar - i) in s:
    #         flag=True
    #         return
    #     s.add(i)
    # if flag==True:
    #     print(ind+1)
    # else:
    #     print(-1)

for _ in range(int(input())):
   main()

