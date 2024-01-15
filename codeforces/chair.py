def main():
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        if a[i]==i+1:
            c+=1
    # print(c)
    if c%2==0:
        print(c//2)
    else:
        print(1+c//2)


for _ in range(int(input())):
    main()