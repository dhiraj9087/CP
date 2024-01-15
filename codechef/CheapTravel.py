def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    for i in range(n-k):
        if a[i]>a[i+k]:
            a[i],a[i+k]=a[i+k],a[i]
    print(*a)
for _ in range(int(input())):
    main()