def main():
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    s=0
    c=0
    for i in range(n):
        s+=a[i]
        c+=1
        if (s)<x*(i+1):
            c-=1
            # print(add[i])
    print(c)
    # print(0 if c==0 else c+1)
    # n, m = map(int, input().split())
    # arr = list(map(int, input().split()))
    # arr.sort(reverse=True)
    # count = 0
    # sum = 0
    # for i in range(n):
    #     sum += arr[i]
    #     count += 1
    #     product = count * m
    #     if sum < product:
    #         count -= 1
    #         break
    # print(count)
for _ in range(int(input())):
    main()