# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avg = []
        if root:
            queue = deque([root])
            while queue:
                total_val = 0
                total_node = len(queue)

                for _ in range(total_node):
                    node = queue.popleft()
                    total_val += node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                
                avg.append(total_val/total_node)
        return avg        
