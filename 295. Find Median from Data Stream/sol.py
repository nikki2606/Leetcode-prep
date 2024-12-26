from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.min_heap = [] # all the larger numbers
        self.max_heap = [] # all the min numbers

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0 or num < self.min_heap[0]:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
        
        # balance both the heaps such that len(min_heap) >= len(max_heap)
        if len(self.max_heap) < len(self.min_heap):
            val = heappop(self.min_heap)
            heappush(self.max_heap, -val)
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = heappop(self.max_heap)
            heappush(self.min_heap, -val)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0]+self.min_heap[0])/2
        elif len(self.max_heap) > 0:
            return -self.max_heap[0]
        return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()