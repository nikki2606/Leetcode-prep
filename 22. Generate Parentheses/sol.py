class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(start, path, open_count, close_count):
            if start == 2*n:
                res.append("".join(path))
                return
            
            for char in "()":
                # prune
                if char == "(" and open_count >= n:
                    continue
                elif char == ")" and close_count >= open_count:
                    continue

                # append
                path.append(char)

                # additional checks
                if char == "(":
                    open_count += 1
                else:
                    close_count += 1
                
                # dfs
                dfs(start+1, path, open_count, close_count)

                # remove additional checks
                if char == "(":
                    open_count -= 1
                else:
                    close_count -= 1
                
                # pop
                path.pop()

        dfs(0, [], 0, 0)
        return res