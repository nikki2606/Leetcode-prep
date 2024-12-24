class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            self.prefix_sum.append(cur_sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right] if left == 0 else self.prefix_sum[right]-self.prefix_sum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)