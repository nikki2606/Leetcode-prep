class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return 0

        stack = []
        for char in s:
            if stack:
                if char == ")" and stack[-1] == "(":
                    val = stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        
        if stack:
            return len(stack)
        return 0