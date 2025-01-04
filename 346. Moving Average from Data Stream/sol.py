from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.window_sum += val
        n = len(self.queue)
        if n <= self.size:
            return self.window_sum/n
        removed = self.queue.popleft()
        self.window_sum -= removed
        return self.window_sum/self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)