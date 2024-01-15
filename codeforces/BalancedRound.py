import sys
input=sys.stdin.readline

def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    # a.sort()
    # # print(a)
    # ans,c=0,1
    # for i in range(1,n):
    #     if a[i]-a[i-1] <=k:
    #         c+=1
    #     else:
    #         ans = max(ans,c)
    #         c=1
    # ans = max(ans,c)
    # print(n-ans)
    
    
for _ in range(int(input())):
    main()

