class SnapshotArray:

    def __init__(self, n: int):
        self.snapshot_id = 0
        self.arr = [[[-1, 0]] for _ in range(n)]

    def set(self, index: int, val: int) -> None:
        self.arr[index].append([self.snapshot_id, val])

    def snap(self) -> int:
        self.snapshot_id += 1
        return self.snapshot_id - 1

    def get(self, index: int, snap_id: int) -> int:
        left, right = 0, len(self.arr[index])-1
        pos = -1
        while left <= right:
            mid = (left+right)//2
            if self.arr[index][mid][0] <= snap_id:
                pos = mid
                left = mid + 1
            else:
                right = mid - 1
        return self.arr[index][pos][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)