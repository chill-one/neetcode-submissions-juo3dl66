class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        length = max(len(word1), len(word2))

        res = []
        for i in range(length):
            first = "" if i >= len(word1) else word1[i]
            second = "" if i >= len(word2) else word2[i]

            if first:
                res.append(first)

            if second:
                res.append(second)


        return "".join(res)