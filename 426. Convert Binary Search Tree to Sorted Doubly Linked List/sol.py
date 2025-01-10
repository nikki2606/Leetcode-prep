"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
from collections import deque

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        queue = deque([])
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            queue.append(Node(root.val))
            inorder(root.right)
        
        inorder(root)
        head = queue.popleft()
        node = head

        while queue:
            node2 = queue.popleft()
            node.right = node2
            node2.left = node
            node = node.right
        
        node.right = head
        head.left = node
        return head