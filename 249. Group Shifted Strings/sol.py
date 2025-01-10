class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        if not strings:
            return []

        shift = {}
        res = []
        for s in strings:
            if s[0] == "a":
                if s not in shift:
                    shift[s] = []
                shift[s].append(s)
            else:
                change = ord(s[0])-ord('a')
                temp = ""
                for i in range(len(s)):
                    changeVal = ord(s[i])-change
                    if changeVal < ord('a'):
                        changeVal += 26
                    temp = temp + chr(changeVal)
                if temp not in shift:
                    shift[temp] = []
                shift[temp].append(s)

        for s,slist in shift.items():
            res.append(slist)
        
        return res
                