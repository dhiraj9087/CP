# grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
def island(i,j):
    if i<0 or j<0:
        return
    if i>=n or j>=m:
        return
    if grid[i][j]=='0':
        return
    grid[i][j]='0'
    island(i,j-1)
    island(i,j+1)
    island(i+1,j)
    island(i-1,j)


n=len(grid)
m=len(grid[0])
ans=0
for i in range(n):
    for j in range(m):
        if grid[i][j]=='0':
            continue
        ans+=1
        island(i,j)
print(ans)
