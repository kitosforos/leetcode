class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c != "." and c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True
        return None

    def search(self, word: str) -> bool:
        node = self.root

        def dfs(node, word):
            for i, c in enumerate(word):
                if c == ".":
                    for n in node.children.values():
                        if dfs(n, word[i + 1:]) == True:
                            return True
                    return False
                else:
                    if c not in node.children:
                            return False
                    node = node.children[c]
            print(node.end)
            return node.end

        return dfs(node, word)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)