# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        rtest=deque()
        rtest.append(root)
        while len(rtest)!=0:
            templ=[]
            for _ in range(len(rtest)):
                rtv=rtest.popleft()
                templ.append(rtv.val)
                if rtv.left:
                    rtest.append(rtv.left)
                if rtv.right:
                    rtest.append(rtv.right)
        
        return sum(templ)


