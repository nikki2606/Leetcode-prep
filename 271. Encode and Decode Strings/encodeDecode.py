class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ''
        for s in strs:
            res += s+ '\n'
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i<len(s):
            sstr = ''
            while s[i] != '\n':
                sstr += s[i]
                i += 1
            i += 1
            res.append(sstr)
        return res
            


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

### Notes
# Time: O(n)
# Space: O(n)