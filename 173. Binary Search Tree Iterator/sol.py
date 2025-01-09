# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.bstArr = []
        self.i = 0
        self.inorder(root)


    def inorder(self, root):
        if not root:
            return
        
        self.inorder(root.left)
        self.bstArr.append(root.val)
        self.inorder(root.right)


    def next(self) -> int:
        if not self.bstArr or self.i >= len(self.bstArr):
            return 0

        val = self.bstArr[self.i]
        self.i += 1
        return val
        

    def hasNext(self) -> bool:
        return self.i < len(self.bstArr)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()