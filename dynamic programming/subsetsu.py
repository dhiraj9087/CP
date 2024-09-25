arr=[2,3,7,8,10]
tar=11
dp = [[False for _ in range(tar+1)] for _ in range(len(arr)+1)]
for i in range(len(arr)+1):
    for j in range(tar+1):
        if i==0:
            dp[i][j]=False
        if j==0:
            dp[i][j]=True
# print(dp)




def sub(ind,tar):
    if tar==0:
        return True
    if ind==0:
        return tar==arr[0]
    nottake = sub(ind-1,tar)
    take = False
    if tar>=arr[ind]:
        take = sub(ind-1,tar-arr[ind])
    return take or nottake
    



arr=[2,3,7,8,10]
tar=11
n=len(arr)
ans=[]
s=0
sub(n,tar)