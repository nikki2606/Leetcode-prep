# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        depth = 0
        while len(queue) > 0:
            n = len(queue)
            depth += 1
            for i in range(n):
                node = queue.popleft()
                if node:
                    if not node.left and not node.right:
                        return depth
                    
                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)
        return depth