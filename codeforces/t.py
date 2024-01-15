def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ans=[]
    rem =[]
    # for i in range(n):
    #     if a[i]%k==0:
    #         ans.append(i+1)
    #     else:
    #         rem.append((a[i]%k,i+1))
    # rem.sort()
    # # print(rem,ans)
    # for i in range(len(rem)):
    #     ans.append(rem[i][1])
    # print(*ans)
    # ans=[]
    # pair=[]
    # for i in range(n):
    #     pair.append((rem[i],i+1))
    # pair.sort()
    # # print(pair)
    # for i in range(len(pair)):
    #     print(pair[i][1],end=' ')
    # print()
    
    for i in range(n):
        rem.append((a[i],-(i+1)))
    # print(rem)
    fin=[]
    for i in range(n):
        if rem[i][0] % k==0:
            ans.append(-rem[i][1])
        else:
            fin.append((rem[i][0] % k, rem[i][1]))
    # print(ans,fin)
    fin.sort(reverse=True)
    # print(fin)
    for i in range(len(fin)):
        ans.append(-fin[i][1])
    print(*ans)
for _ in range(int(input())):
    main()

