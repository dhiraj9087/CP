def main():
    n=int(input())
    c=0
    i=1
    a=set()
    while i*i<=1e+7:
        if n%i == 0:
            c+=1
            a.add(i)
            if i!=n//i:
                a.add(n//i)
                c+=1
        i+=1
    a=list(a)
    a.sort()
    # print(a)
    # if len(a)==c:
    #     print(1)
    #     return
    maxi=float('-inf')
    q=1
    for i in range(len(a)-1):
        if a[i]+1==a[i+1]:
            q+=1
            maxi=max(maxi,q)
        else:
            q=1
    # print(maxi)
    if maxi>0:
        print(maxi)
    else:
        print(1)
    # l,r=0,1
    # while r<1e+7:
    #     if l%n==0:




for _ in range(int(input())):
    main()

