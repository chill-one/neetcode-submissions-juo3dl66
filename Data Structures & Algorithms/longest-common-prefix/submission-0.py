class TrieNode:
    def __init__(self):
        self.children = {}
        self.done = False

class Solution:

    def add(self, root, word):
        curr = root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]

        curr.done = True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = TrieNode()

        for word in strs:
            self.add(root, word)

        res = []
        curr = root
        for char in strs[0]:
            if char not in curr.children or curr.done or len(curr.children) != 1:
                break
            res.append(char)
            curr = curr.children[char]
        
        return "".join(res)

        


