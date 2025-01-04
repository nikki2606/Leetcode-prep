class Solution:
    def sum(self, a: int, b: int) -> int:
        while b != 0:
        # Increment or decrement 'a' and 'b'
            if b > 0:
                a += 1
                b -= 1
            elif b < 0:
                a -= 1
                b += 1
    
        return a