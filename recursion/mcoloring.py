from collections import defaultdict
from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
    
        for u,v in paths:
            graph[u].append(v)
            graph[v].append(u)
        col=[0]*(n+1)
        def safe(node,paths,col,n,m):
            for nei in paths[node]:
                if col[nei]==m:
                    return False
            return True


        def solve(node,paths,col,n,m):
            if node==n+1:
                return True
            for i in range(1,5):
                if safe(node,paths,col,n,i):
                    col[node]=i
                    if solve(node+1,paths,col,n,m)==True:
                        return True
                    col[node]=0
            return False




        solve(1,graph,col,n,4)
        return col[1:]
        
