class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return ""
        
        res = ""
        stack = []
        for char in s:
            if stack:
                if stack[-1] == char:
                    val = stack.pop()
                    continue
            stack.append(char)
        
        while stack:
            val = stack.pop()
            res = val + res
        return res