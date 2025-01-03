class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[[0,0]] for i in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id-1

    def get(self, index: int, snap_id: int) -> int:
        left, right = 0, len(self.arr[index])-1
        res = 0
        while left <= right:
            mid = (left+right)//2
            if self.arr[index][mid][0] <= snap_id:
                res = self.arr[index][mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)