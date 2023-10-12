# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        ans = []
        d = 0
        while queue:
            curr_length = len(queue)
            curr = []
            
            for i in range(curr_length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                if d%2 == 0:
                    curr.append(node.val)
                else:
                    curr.insert(0,node.val)
            d+=1
            ans.append(curr)
        return ans
                
