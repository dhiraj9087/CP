def main():
    n,k,l=map(int,input().split())
    d=[]
    for i in range(n):
        a,b=map(int,input().split())
        if b==l:
            d.append(a)
    d.sort(reverse=True)
    m=0
    if len(d)==0 or k > len(d):
        print(-1)
        return
    if k==1:
        print(d[0])
        return
    for i in range(k):
        m=m+d[i]
    print(m)
for _ in range((int(input()))):
    main()
    