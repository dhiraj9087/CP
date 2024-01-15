def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    # print(a)
    m=max(a)
    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    # print(d)
    for i in range(m):
        if d.get(i,0)<d.get(i+1,0):
            print("NO")
            return
    print("YES")
for _ in range(int(input())):
    main()
    