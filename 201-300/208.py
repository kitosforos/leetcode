class TrieNode:
    def __init__(self):
        self.ch = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.ch:
                node.ch[c] = TrieNode()
            node = node.ch[c]
        node.end = True

        return None

    def search(self, word: str) -> bool:
        node = self.root

        for c in word:
            if c not in node.ch:
                return False
            node = node.ch[c]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for c in prefix:
            if c not in node.ch:
                return False
            node = node.ch[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)