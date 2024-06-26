# Time: O(n) Space: O(n)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left <= right:
            if s[left] != s[right]:
                return self.isPalindrome(left+1,right,s) or self.isPalindrome(left,right-1,s)
            left += 1
            right -= 1
        return True

    def isPalindrome(self, start, end, s):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True