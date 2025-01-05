class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        if not sentence:
            return ""

        words = sentence.split(" ")
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        for i in range(len(words)):
            if words[i][0] not in vowels:
                first = words[i][0]
                words[i] = words[i][1:] + first
            words[i] += ("ma" + "a"*(i+1))
        
        return " ".join(words)