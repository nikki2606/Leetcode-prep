class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        left, right = 0, len(self.calendar)-1
        idx = len(self.calendar)
        while left <= right:
            mid = (left+right)//2
            if self.calendar[mid][0] > startTime:
                idx = mid
                right = mid - 1
            else:
                left = mid + 1
        if (idx > 0 and self.calendar[idx-1][-1] > startTime) or (idx < len(self.calendar) and self.calendar[idx][0] < endTime):
            return False
        self.calendar.insert(idx, (startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)