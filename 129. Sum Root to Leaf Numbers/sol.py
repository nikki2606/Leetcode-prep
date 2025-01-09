# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        summ = 0
        stack = [(root, 0)]
        while stack:
            root, curnum = stack.pop()
            if root is not None:
                curnum = curnum*10 + root.val
                if root.left is None and root.right is None:
                    summ += curnum
                else:
                    stack.append((root.left, curnum))
                    stack.append((root.right, curnum))
        return summ