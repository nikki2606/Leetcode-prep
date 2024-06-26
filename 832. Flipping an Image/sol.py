# Time: O(n*m) Space: O(1)
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            # flip
            l, r = 0, len(image[0])-1
            while l <= r:
                image[i][l], image[i][r] = image[i][r], image[i][l]
                l += 1
                r -= 1
            
            # invert
            for j in range(len(image[0])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0

        return image