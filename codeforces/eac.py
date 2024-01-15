def main():
    n,m,k,H=map(int,input().split())
    h=list(map(int,input().split()))
    ans=0
    # count = 0
    diff_h=[H-h[i] for i in range(n)]
    steps=[i*k for i in range(1,m+1)]
    diff_s=[]
    for i in range(len(steps)):
        for j in range(i+1,len(steps)):
            diff_s.append(abs(steps[i]-steps[j]))
    # print(diff_s)
    ans=0
    for i in range(len(diff_h)):
        if diff_h[i] in diff_s:
            ans+=1
    print(ans)




for _ in range(int(input())):
    main()