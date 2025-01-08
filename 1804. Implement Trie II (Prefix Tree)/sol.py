class TrieNode:
    def __init__(self):
        self.children = {}
        self.freq = 0
        self.countWords = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node.countWords += 1
            node = node.children[w]
        node.freq += 1
        node.countWords += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for w in word:
            if w not in node.children:
                return 0
            node = node.children[w]
        return node.freq

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for w in prefix:
            if w not in node.children:
                return 0
            node = node.children[w]
        return node.countWords

    def erase(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                return
            node.countWords -= 1
            node = node.children[w]
        node.freq -= 1
        node.countWords -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)