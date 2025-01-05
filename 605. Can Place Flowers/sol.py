class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        flowers = 0

        if n == 0:
            return True

        if length < 2:
            return not bool(flowerbed[0])

        for i in range(length):
            if flowerbed[i] == 0:
                empty_left = (i==0) or (flowerbed[i-1] == 0)
                empty_right = (i == length-1) or (flowerbed[i+1] == 0)

                if empty_left and empty_right:
                    flowerbed[i] = 1
                    flowers += 1

        return flowers >= n