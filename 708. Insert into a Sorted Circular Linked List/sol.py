"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new = Node(insertVal)
        if not head:
            head = new
            new.next = head
            return head
        
        if head.next == head:
            head.next = new
            new.next = head
            return head
        
        prev = head
        curr = head.next

        while curr != head:
            if (prev.val <= insertVal <= curr.val) or (prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val)):
                prev.next = new
                new.next = curr
                return head
            prev = prev.next
            curr = curr.next
        
        prev.next = new
        new.next = curr
        return head