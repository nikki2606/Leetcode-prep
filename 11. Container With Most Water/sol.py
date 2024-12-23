class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        if not height:
            return 0

        left, right = 0, len(height)-1

        while left < right:
            area = max(area, min(height[right],height[left])*abs(right-left))
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return area