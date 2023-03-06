class Node:
    def __init__(self, v: str, end = False):
        self.value = v
        self.child = {}
        self.end = end

class Trie:
    def __init__(self):
        self.root = Node(None)


    def insert(self, word: str) -> None:
        p = self.root
        l = len(word)
        i = -1
        for i in range(l - 1):
            if word[i] not in p.child:
                p.child[word[i]] = Node(word[i])
            p = p.child[word[i]]
        i += 1
        if word[i] not in p.child:
            p.child[word[i]] = Node(word[i], True)
        else:
            p.child[word[i]].end = True


    def search(self, word: str) -> bool:
        p = self.root
        l = len(word)
        i = -1
        for i in range(l - 1):
            if word[i] not in p.child:
                return False
            p = p.child[word[i]]
        i += 1
        if word[i] not in p.child:
            return False
        return p.child[word[i]].end



    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for i in prefix:
            if i not in p.child:
                return False
            p = p.child[i]
        return True