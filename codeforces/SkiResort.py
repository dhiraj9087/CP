def main():
    n,k,q=map(int,input().split())
    a=list(map(int,input().split()))
    mini=min(a)
    maxi=max(a)
    if mini>q:
        print(0)
        return
    count1,count2=0,0
    count=0
    f=0
    for i in range(n):
        if a[i]<=q:
            count1+=1
        else:
            count1=0
        if count1>=k:
            count+=count1-k+1
    print(count)
    # for i in 
for _ in range(int(input())):
    main()
    
