# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            
            left_path = dfs(root.left)
            right_path = dfs(root.right)

            self.diameter = max(self.diameter, left_path+right_path)
            return 1 + max(left_path, right_path)
        
        val = dfs(root)
        return self.diameter