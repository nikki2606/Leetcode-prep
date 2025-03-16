class TrieNode:
    def __init__(self):
        self.children = {}
        self.freq = 0

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        n = len(strs)
        
        data = TrieNode()
        for s in strs:
            node = data
            for char in s:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.freq += 1
        
        node = data
        res = ""
        while node:
            if len(node.children) != 1:
                return res
            char = next(iter(node.children))
            node = node.children[char]
            if node.freq != n:
                return res
            res = res + char
        return ""
    
    # Time: O(n*m)
    # Space: O(n*m)