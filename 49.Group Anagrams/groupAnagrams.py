from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        res = []
        anagram = {}
        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word not in anagram:
                anagram[sorted_word] = []
            anagram[sorted_word].append(word)
        
        for key, ana in anagram.items():
            res.append(ana)
        
        return res