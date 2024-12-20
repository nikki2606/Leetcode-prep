class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterDict = {"2":"abc", "3": "def",
        "4": "ghi", "5": "jkl", "6": "mno",
        "7" : "pqrs", "8": "tuv", "9": "wxyz"}

        res = []
        if not digits:
            return res

        def dfs(start, path, res):
            if start == n:
                res.append("".join(path))
                return
            
            digit = digits[start]
            for char in letterDict[digit]:
                path.append(char)
                dfs(start+1, path, res)
                path.pop()

        n = len(digits)
        dfs(0, [], res)
        return res