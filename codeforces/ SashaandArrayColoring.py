def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    f,l=0,n-1
    mid=n//2
    ans=0
    while mid>0:
        left=a[f]
        right=a[l]
        r=right-left
        ans+=r
        mid-=1
        f+=1
        l-=1
    
    print(ans)
for _ in range(int(input())):
    main()