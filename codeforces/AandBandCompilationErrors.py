def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    a.sort()
    b.sort()
    c.sort()
    # print(a)
    # print(b)
    # print(c)
    flag=True
    for i in range(n-1):
        if a[i]!=b[i]:
            print(a[i])
            flag=False
            break
    if flag==True:
        print(a[n-1])
    flag=True
    for i in range(n-2):
        if b[i]!=c[i]:
            print(b[i])
            flag=False
            break
    if flag==True:print(b[n-2])

            
    # q,w=0,0
    # for i in range(n):
    #     if a[i] not in b:
    #         q=a[i]
    # for i in range(n-1):
    #     if b[i] not in c:
    #         w=b[i]

main()