from collections import Counter
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arrset = Counter(arr)
        for num in arr:
            if num*2 in arrset:
                if num == 0 and arrset[num] < 2:
                    continue
                return True
        return False