class TrieNode:

    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()

        # insert in Trie
        for i, sentence in enumerate(sentences):
            self.insert(sentence, times[i])

        self.curr_node = self.root
        self.curr_sentence = []

    def insert(self, sentence, time):
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.sentences[sentence] += time
                

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.curr_node = self.root
            sentence = "".join(self.curr_sentence)
            self.curr_sentence = []
            self.insert(sentence, 1)
            return []

        self.curr_sentence.append(c)
        if c not in self.curr_node.children:  
            self.curr_node = TrieNode()
            return []

        self.curr_node = self.curr_node.children[c]
        sentences = self.curr_node.sentences
        sorted_sentences = sorted(sentences.items(), key=lambda x:(-x[1], x[0]))
        res = []
        for i in range(min(3, len(sorted_sentences))):
            res.append(sorted_sentences[i][0])
        return res
        



# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)