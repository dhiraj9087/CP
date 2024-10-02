from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(row,col,board):
            duprow=row
            dupcol=col
            while row>=0 and col>=0:
                if board[row][col]=='Q':
                    return False
                row-=1
                col-=1
            row=duprow
            col=dupcol
            while col>=0:
                if board[row][col]=='Q':
                    return False
                col-=1
            row = duprow
            col = dupcol
            while row<n and col>=0:
                if board[row][col]=='Q':
                    return False
                row+=1
                col-=1
            return True
        def solve(col,board,ans):
            if col==n:
                ans.append([''.join(row) for row in board])
                return
            for row in range(n):
                if is_safe(row,col,board)==True:
                    board[row][col] = 'Q'
                    solve(col+1,board,ans)
                    board[row][col] = '.'
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans=[]
        solve(0,board,ans)
        return ans








