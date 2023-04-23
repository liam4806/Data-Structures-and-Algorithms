# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        else:
            levelq=deque()
            levelq.append(root)
            result=[]
            while len(levelq)!=0:
                templ=[]
                for _ in range(len(levelq)):
                    rt=levelq.popleft()
                    templ.append(rt.val)
                    if rt.left is not None:
                        levelq.append(rt.left)
                    if rt.right is not None:
                        levelq.append(rt.right)
                result.append(templ)
            return result                    

