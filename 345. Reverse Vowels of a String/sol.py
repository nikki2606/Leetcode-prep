# Time: O(n) Space: O(n)
class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        left, right = 0, len(s)-1
        sList = list(s)
        while left <= right:
            if not self.isVowel(s[left]):
                left += 1
                continue
            
            if not self.isVowel(s[right]):
                right -= 1
                continue

            if left < len(s) and right >= 0:
                sList[left], sList[right] = sList[right], sList[left]
            left += 1
            right -= 1
        
        return ''.join(sList)
    
    def isVowel(self, char):
        char = char.lower()
        vowel = set(['a','e','i','o','u'])
        if char in vowel:
            return True
        return False