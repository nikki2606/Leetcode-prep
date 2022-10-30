class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Time: O(n)
        carry = sumInPlace = 0
        for i in range(len(digits)-1,-1,-1):
            if i == len(digits)-1:
                sumInPlace = digits[i] + 1
            else:
                sumInPlace = digits[i] + carry
            digits[i] = sumInPlace % 10
            carry = sumInPlace//10
            
        if carry != 0:
            digits.insert(0, carry)
        
        return digits