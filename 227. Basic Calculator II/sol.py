class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        stack = []
        n = len(s)
        i = 0
        sign = 1
        operator = ""
        while i < n:
            if s[i] == "+":
                sign = 1
                i += 1
            elif s[i] == "-":
                sign = -1
                i += 1
            elif s[i] == "*":
                operator = "*"
                i += 1
            elif s[i] == "/":
                operator = "/"
                i += 1
            elif s[i].isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num*10 + int(s[i])
                    i += 1
                num = sign*num
                stack.append(num)
                sign = 1
                if operator and stack:
                    b = stack.pop()
                    a = stack.pop()
                    c = 0
                    if operator == "*":
                        c = a*b
                    elif operator == "/":
                        if (a>=0 and b>0) or (a<0 and b<0):
                            sign = 1
                        else:
                            sign = -1
                        
                        c = abs(a)//abs(b)
                        c = sign*c
                    operator = ""
                    sign = 1
                    stack.append(c)
            else:
                i += 1
        res = 0
        while stack:
            res += stack.pop()
        return res
