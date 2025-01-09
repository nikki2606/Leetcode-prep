"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # create all nodes of node2 and map then to node1 in Dict, including None
        nodeDict = {None: None}
        node1 = head

        while node1:
            nodeDict[node1] = Node(node1.val)
            node1 = node1.next
        
        # parse through node1 and connect node2
        node1 = head
        head2 = nodeDict[node1]
        node2 = head2
        while node1:
            node2.next = nodeDict[node1.next]
            node2.random = nodeDict[node1.random]
            node2 = node2.next
            node1 = node1.next
        
        return head2