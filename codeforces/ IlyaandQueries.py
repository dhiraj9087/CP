def solve():
    s=input()
    pre_sum=[0]*len(s)
    c=0
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            c+=1
        pre_sum[i]=c
    # print(pre_sum)
    n=int(input())
    a=[]
    for i in range(n):
        l,r=map(int,input().split())
        a.append(pre_sum[r-1]-pre_sum[l-1])
    print(*a,sep='\n')
solve()
