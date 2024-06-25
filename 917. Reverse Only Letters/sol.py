# Time: O(n) Space: O(n)
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        left, right = 0, len(s)-1
        sList = list(s)
        while left <= right:
            if not sList[left].isalpha():
                left += 1
                continue
            
            if not sList[right].isalpha():
                right -= 1
                continue
            
            if left < len(s) and right >= 0:
                sList[left], sList[right] = sList[right], sList[left]
            left += 1
            right -= 1

        return ''.join(sList)