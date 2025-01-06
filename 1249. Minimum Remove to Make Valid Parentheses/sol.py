class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return ""
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == ")":
                if stack:
                    if stack[-1][0] == "(":
                        val = stack.pop()
                    else:
                        stack.append([s[i], i])
                else:
                    stack.append([s[i], i])
            elif s[i] == "(":
                stack.append([s[i], i])
        
        res = ""
        id = set()
        while stack:
            char, idx = stack.pop()
            id.add(idx)
        
        for i in range(n):
            if i not in id:
                res += s[i]
        
        return res