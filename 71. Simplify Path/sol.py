class Solution:
    def simplifyPath(self, path: str) -> str:
        pathList = path.split("/")

        res = []
        for i, dir in enumerate(pathList):      
            if dir == "..":
                if res:
                    val = res.pop()
            elif dir == "." or dir == "":
                continue
            else:
                res.append(dir)
        
        return "/"+"/".join(res)
