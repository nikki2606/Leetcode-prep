class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n = max(len(num1), len(num2))
        num1 = num1.zfill(n)
        num2 = num2.zfill(n)
        carry = 0
        res = ""

        for i in range(n-1,-1,-1):
            digitsum = int(num1[i]) + int(num2[i]) + carry
            carry = digitsum//10
            digit = digitsum%10
            res = str(digit) + res
        
        if carry:
            res = str(carry) + res
        
        return res