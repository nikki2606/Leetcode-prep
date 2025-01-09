class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if not word and not abbr:
            return True

        if not word or not abbr:
            return False

        i, j = 0, 0
        n, m = len(word), len(abbr)
        while i<n and j<m:
            if abbr[j].isdigit():
                if abbr[j] == "0":
                    return False

                cursum = 0
                while j < m and abbr[j].isdigit():
                    cursum = cursum*10 + int(abbr[j])
                    j += 1
                i += cursum
            else:
                if word[i] != abbr[j]:
                    return False
                j += 1
                i += 1
               
        
        return i == n and j == m