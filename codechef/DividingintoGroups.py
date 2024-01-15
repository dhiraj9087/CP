def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    print(a)
    flag=True
    while flag:
        for i in range(k):
            a[i]-=k
            


for _ in range((int(input()))):
    main()