class TimeMap:

    def __init__(self):
        self.datastore = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.datastore:
            self.datastore[key] = []
        self.datastore[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.datastore:
            return ""
        
        left, right = 0, len(self.datastore[key])-1
        closest_timestamp = -1
        while left <= right:
            mid = (left+right)//2
            if self.datastore[key][mid][0] <= timestamp:
                closest_timestamp = mid
                left = mid + 1
            else:
                right = mid - 1
        if closest_timestamp == -1:
            return ""
        return self.datastore[key][closest_timestamp][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)