# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #base case
        if not q and not p:
            return True
        elif not p:
            return False
        elif not q:
            return False
        if q.val==p.val:
            return self.isSameTree(q.left,p.left) and self.isSameTree(q.right,p.right)
        


        
