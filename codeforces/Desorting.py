import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    # q=sorted(a)
    # if q!=a:
    #     print(0)
    #     return
    # if (a[n-1]-a[n-2])==0:
    #     print(1)
    #     return
    # print((a[n-1]-a[n-2]+1)//2)
    q=[]
    for i in range(n-1):
        q.append(a[i+1]-a[i])
    # print(q)
    ans=min(q)
    # print(ans)
    if ans<0:
        print(0)
        return
    if ans==0:
        print(1)
        return
    print((ans//2)+1)

for _ in range(int(input())):
    main()