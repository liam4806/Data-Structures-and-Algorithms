# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        que4p= deque()
        que3q= deque()
        que4p.append(p)
        que3q.append(q)
        while len(que4p)!=0:
            x=que4p.pop()
            y=que3q.pop()
            if x is None and y is not None:
                return False
            if x is not None and y is None:
                return False
            if x is None and y is None:
                continue
            if x.val != y.val:
                return False
            que4p.append(x.left)
            que3q.append(y.left)
            que4p.append(x.right)
            que3q.append(y.right)
        return True