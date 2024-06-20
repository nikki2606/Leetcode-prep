# Time: O(nm) Space: O(n+m)
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsDict = defaultdict(int)
        for char in chars:
            charsDict[char] += 1
        
        res = 0
        for word in words:
            wordCount = defaultdict(int)
            for char in word:
                wordCount[char] += 1
            
            good = True

            for w, freq in wordCount.items():
                if charsDict[w] < freq:
                    good = False
                    break

            if good:
                res += len(word)
        
        return res