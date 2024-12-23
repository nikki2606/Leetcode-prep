# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = deque([root])
        while len(queue) > 0:
            n = len(queue)
            level = []
            for i in range(n):
                node = queue.popleft()
                if node:
                    for child in [node.right, node.left]:
                        queue.append(child)
                    level.append(node.val)
            if level:
                res.append(level[0])

        return res