grid = [[1,2],[3,4]]
# grid = [[12345],[2],[1]]
n=len(grid)
m=len(grid[0])
ans=grid
pro=1
mod=12345
for i in range(n):
    for j in range(m):
        pro*=grid[i][j]
for i in range(n):
    for j in range(m):
        ans[i][j]=(pro//grid[i][j])%mod
print(pro,ans)