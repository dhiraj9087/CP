from typing import List
from math import inf
from collections import deque
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V: int, adj: List[List[int]], S: int) -> List[int]:
    # Code here
        dist=[inf]*V
        dist[S]=0
        q=deque()
        q.append(S)
        while q:
            node = q.popleft()
            for ver,weight in adj[node]:
                if dist[node] + weight < dist[ver]:
                    dist[ver] = dist[node] + weight
                    q.append(ver)
        return dist
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        S = int(input())
        ob = Solution()

        res = ob.dijkstra(V, adj, S)
        for i in res:
            print(i, end=" ")
        print()

# } Driver Code Ends