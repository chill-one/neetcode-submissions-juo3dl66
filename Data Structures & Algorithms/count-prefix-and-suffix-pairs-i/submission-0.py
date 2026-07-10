class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            first = words[i]
            for j in range(i + 1, len(words)):
                second = words[j]

                if second.startswith(first) and second.endswith(first):
                    count += 1



        return count