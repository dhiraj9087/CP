for i in range((int(input()))):
    n,k=map(int,input().split())
    if n%k==0:
        print("YES")
    elif n%2==0 and k%2==0:
        print("YES")
    elif n%2==1 and k%2==0:
        print("NO")
    elif n%2==0 and k%2==1:
        print("YES")
    else:
        print("YES")

