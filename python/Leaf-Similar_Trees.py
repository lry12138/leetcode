# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leave_search(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            
            return leave_search(root.left) + leave_search(root.right)

        return leave_search(root1)==leave_search(root2)
        
