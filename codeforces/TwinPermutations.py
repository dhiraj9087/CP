def main():
    n=int(input())
    a=list(map(int,input().split()))
    # b=[i for i in range(1,n+1)]
    # for i in range(n-1):
    #     if a[i]+b[i]>a[i+1]+b[i+1]:
    #         b[i],b[i+1]=b[i+1],b[i]
    # print(b)
    for i in range(n):
        print(n - a[i] + 1, end=" ")
    print()

for _ in range((int(input()))):
    main()