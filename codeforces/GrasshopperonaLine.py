def main():
    n=int(input())
    a=list(map(int,input().split()))
    # first=a[0]
    # # maxi=max(a)
    # ans=float('-inf')
    # for i in range(1,n):
    #         first ^= a[i]
    #         ans=max(ans,first)
    # print(ans)
    # if a[n-1]==maxi:
    #     for i in range(1,n):
    #         first ^= a[i]
    # else:
    #     for i in range(1,n-1):
    #         first ^= a[i]
    
 
    S = set()
    res = 0
    for num in a:
        newS = set()
        res = max(res, num)
        newS.add(num)
 
        for ele in S:
            res = max(res, ele ^ num)
            newS.add(ele ^ num)
        S = newS
    
    print(res)
    
for _ in range(int(input())):
    main()

    