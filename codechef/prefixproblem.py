for i in range((int(input()))):
    n=int(input())
    lst=[i for i in range(1,n+1)]
    if n%2!=0:
        print("-1")
    else:
        for i in range(2,n,2):
            lst[i],lst[i+1]=lst[i+1],lst[i]
        for i in lst:
            print(i,end=" ")
        print()

    

