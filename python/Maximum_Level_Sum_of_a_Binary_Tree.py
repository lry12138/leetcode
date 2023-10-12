# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if root:
            level = 1
            max_sum = float("-inf")
            queue = deque([root])
            while queue:
                curr = 0 
                for i in range(len(queue)):
                    node = queue.popleft()
                    curr += node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                if curr > max_sum:
                    ans = level
                    max_sum = curr
                level+=1

        return ans
