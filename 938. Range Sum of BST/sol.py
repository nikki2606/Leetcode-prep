# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            if root.val >= low and root.val <= high:
                self.sum += root.val
            inorder(root.right)
        
        inorder(root)
        return self.sum