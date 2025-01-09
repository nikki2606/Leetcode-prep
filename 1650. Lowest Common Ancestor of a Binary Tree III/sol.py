"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if not p or not q:
            return None

        ancestors_p = set()
        while p:
            ancestors_p.add(p)
            p = p.parent
        
        while q:
            if q in ancestors_p:
                return q
            q = q.parent
        
        return None