for _ in range((int(input()))):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    mean_a=sum(a)//n
    mean_b=sum(b)//m
    print(mean_a,mean_b)
    i=1
    while mean_a<mean_b:
        a.append(k-i)
        b.append(i)
        i+=1
        mean_a=sum(a)//n
        mean_b=sum(b)//m
        

