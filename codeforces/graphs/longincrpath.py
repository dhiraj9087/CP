import math
import sys
input=sys.stdin.readline
def main():
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp=[[0]*n for i in range(m)]
    ans=0
    def dfs(i,j):
        if dp[i][j]:
            return dp[i][j]
        path=1
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  
            if 0 <= i+x < m and 0 <= j+y < n and matrix[i+x][j+y] > matrix[i][j]:   
                path = max(path, 1 + dfs(i+x, j+y))
        dp[i][j]=path
        return path
    for i in range(n):
        for j in range(m):
            ans=max(ans,dfs(i,j))
    return ans
# for _ in range(int(input())):
main()
