def main():
    n,s,l=8,2,2
    a=[1,0,1,1,0,1,0,1]
    # n,s,l=5,2,3
    # a=[1,1,1,1,1]
    c=0
    k=0
    cnt=a.count(1)
    if l*s>=n:
        print(0)
        return
    for i in range(n):
        if a[i]==1 and k<s:
            for j in range(l):
                a[i]=0
                a[i+j]=0
            k+=1
    print(a)
main()
