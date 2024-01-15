for i in range((int(input()))):
    x,y=map(int,input().split())
    # d=x+y
    ans1,ans2=-1,-1
    for i in range(0,51):
        for j in range(0,51):
            if 2*(i+j)==x+y and 2* (abs(x-i) + abs(y-j)) == x+y:
                ans1,ans2=i,j
                # break
    print(ans1,ans2)
