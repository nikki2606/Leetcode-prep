class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        stack = []
        for char in s:
            if stack:
                if (char == ")" and stack[-1] == "(") or (char == "}" and stack[-1] == "{") or (char == "]" and stack[-1] == "["):
                    val = stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        
        return not stack
