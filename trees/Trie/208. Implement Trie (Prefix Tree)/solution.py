class Node:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for cha in word:
            if not cha in cur.children:
                cur.children[cha] = Node()
            cur = cur.children[cha]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for cha in word:
            if not cha in cur.children:
                return False
            cur = cur.children[cha]
        return cur.word
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for cha in prefix:
            if not cha in cur.children:
                return False
            cur = cur.children[cha]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)