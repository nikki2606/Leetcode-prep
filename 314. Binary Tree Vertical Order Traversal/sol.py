# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([(root, 0)])
        dval = defaultdict(list)
        maxVal, minVal = 0, 0
        while queue:
            node, column = queue.popleft()
            
            if node is not None:
                maxVal = max(maxVal, column)
                minVal = min(minVal, column)
                dval[column].append(node.val)
                queue.append((node.left, column-1))
                queue.append((node.right, column+1))
        
        return [dval[l] for l in range(minVal, maxVal+1)]