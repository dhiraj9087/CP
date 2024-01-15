def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    add=sum(a)
    ans=[add]
    for i in range(n):
        add-=a[i]
        ans.append(add)
    # print(*ans)
    for i in range(len(ans)-1):
        print(ans[i],end=' ')
    print()
for _ in range(int(input())):
    main()