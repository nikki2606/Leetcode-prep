class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0:
            return str(float('inf'))
        
        if numerator == 0:
            return str(0)

        res = []
        if numerator < 0 or denominator < 0:
            if numerator > 0 or denominator > 0:
                res.append("-")
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        res.append(str(numerator//denominator))
        remainder = numerator%denominator

        if remainder == 0:
            return "".join(res)
        
        res.append(".")
        lookup = {}
        while remainder != 0:
            if remainder in lookup:
                res.insert(lookup[remainder], "(")
                res.append(")")
                break
            
            lookup[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder//denominator))
            remainder %= denominator
        return "".join(res)