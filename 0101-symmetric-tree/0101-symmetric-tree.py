# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        t1=root.left
        t2=root.right
        t1d,t2d=deque(),deque()
        t1d.append(t1)
        t2d.append(t2)
        while len(t1d)!=0:
            x=t1d.popleft()
            y=t2d.popleft()
            if x is None and y is None:
                continue
            if x is None or y is None:
                return False
            if x.val != y.val:
                return False
            t1d.append(x.right)
            t1d.append(x.left)
            t2d.append(y.left)
            t2d.append(y.right)
        return True
            
        