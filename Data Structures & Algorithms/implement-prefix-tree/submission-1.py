class Node:
    def __init__(self):
        self.child = [None]*26
        self.done = False

class PrefixTree:
    
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            idx = ord(char) - ord('a')
            if not curr.child[idx]:
                curr.child[idx] = Node()
            curr = curr.child[idx]
        curr.done = True

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            idx = ord(char) - ord('a')
            if not curr.child[idx]:
                return False
            curr = curr.child[idx]
        
        return curr.done
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            idx = ord(char) - ord('a')
            if not curr.child[idx]:
                return False
            curr = curr.child[idx]
        
        return True
        
        