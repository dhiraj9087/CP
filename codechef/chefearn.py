# cook your dish here
for i in range((int(input()))):
    n,a,b=map(int,input().split())
    # print((a*n//2)+(b*n//2))
    q,r=[],[]
    for i in range(0,n+1,2):
        q.append(i)
    for i in range(1,n+1,2):
        r.append(i)
    print((len(q)-1)*a+len(r)*b)
    # print(q,r)