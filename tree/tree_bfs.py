# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import List, Optional
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if not root:
            return ans
        dq = deque()
        dq.append(root)
        while dq:
            size = len(dq)
            level =[]
            for i in range(size):
                node = dq.popleft()
                level.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            ans.append(level)
        return ans