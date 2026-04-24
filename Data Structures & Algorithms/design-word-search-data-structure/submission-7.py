class TrieNode():
    __slots__ = ['child', 'done']
    def __init__(self):
        self.child = {}
        self.done = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.child:
                curr.child[char] = TrieNode()
            curr = curr.child[char]

        curr.done = True

    def search(self, word: str) -> bool:

        def rec(curr, i):
            if i >= len(word):
                return curr.done

            if word[i] == ".":
                for key, value in curr.child.items():
                    if rec(value,i+1):
                        return True
            else:
                if word[i] not in curr.child:
                    return False
                
                if rec(curr.child[word[i]], i+1):
                    return True
                
            return False

        return rec(self.root, 0)
        
