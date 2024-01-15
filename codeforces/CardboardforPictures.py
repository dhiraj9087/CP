import sys
input=sys.stdin.readline
import math
def main():
    n,c=map(int,input().split())
    a=list(map(int,input().split()))
    # # q=math.sqrt(c)
    # add=0
    # s=0
    # ans=0
    # for i in range(n):
    #     add+=(a[i]*a[i])
    #     s+=a[i]
    # # print(c-add)
    # w=c-add
    # # print(s)
    # # print(sum(a))
    # b=2*s
    # rot=math.sqrt((b*b)+(4*n*w))
    # ans = (b + rot)//2*n
    # print(ans//2)
    # n, c = map(int, input().split())
    # v = list(map(int, input().split()))
    # sum = 0
    # sqr = 0
    # for i in v:
    #     sum += i
    #     sqr += i * i
    # i = 1
    # cmp = 0
    # while True:
    #     if cmp == c:
    #         break
    #     cmp = sqr
    #     add = n * (i * i)
    #     cmp += (2 * i) * sum + add
    #     i += 1
    # print((i - 1) // 2)
    i=0
    j=10**9
    # for i in range(j):
    #     add=0
    #     for q in a:
    #         add+=((q+i*2)**2)
    #     if add == c
    #         break
    ans=0
    while i<=j:
        ans=(i+j)//2
        add=0
        for e in a:
            add+= ((e+ans*2)**2)
        if add == c:
            break
        elif add<c:
            i = ans+1
        else:
            j=ans-1
    print(ans)
    
    

for _ in range(int(input())):
    main()