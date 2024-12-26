# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        head = res
        h = []
        for l in lists:
            while l:
                heapq.heappush(h, l.val)
                l = l.next
        while h:
            value = heapq.heappop(h)
            res.next = ListNode(value)
            res = res.next
        return head.next
    
# Time: O(NLogK)