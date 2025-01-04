class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        num = 0
        init = x
        while init > 0:
            rem = init%10
            num = num*10 + rem
            init = init//10
        
        return x == num