def main():
    a=list(map(int,input().split()))
    a.sort()
    if a[1]+a[2]>=10:
        print("YES")
        return
    print("NO")



for _ in range(int(input())):
    main()