class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ref = set(nums)
        max_seq = 0

        for num in ref:
            # check if num is starting number for seq, do this by checking if num-1 exists in the set
            if num-1 not in ref:
                k = 1
                cur_num = num

                while cur_num+1 in ref:
                    k += 1
                    cur_num += 1
                max_seq = max(max_seq, k)
        
        return max_seq