class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        res = []

        def answer(x):
            return a*x**2+b*x+c
        
        left, right = 0, len(nums)-1
        if a < 0:
            while left <= right:
                ansleft = answer(nums[left])
                ansright = answer(nums[right])
                if ansleft < ansright:
                    res.append(ansleft)
                    left += 1
                else:
                    res.append(ansright)
                    right -= 1
        else:
            while left <= right:
                ansleft = answer(nums[left])
                ansright = answer(nums[right])
                if ansleft > ansright:
                    res.append(ansleft)
                    left += 1
                else:
                    res.append(ansright)
                    right -= 1
            res = res[::-1]

        return res