def main():
    n=int(input())
    a=list(map(int,input().split()))
    s=sum(a)
    oddc,evenc=0,0
    count=0
    for i in range(n):
        if a[i]%2==0:evenc+=1
        else:oddc+=1
    if s%2==0:count+=evenc
    else:count+=oddc
    print(count)
    
for _ in range((int(input()))):
    main()
    