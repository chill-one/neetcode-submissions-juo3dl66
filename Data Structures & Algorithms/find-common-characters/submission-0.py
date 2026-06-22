class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        first = Counter(words[0])

        for word in words[1:]:
            first = first & Counter(word)

        return list(first.elements())


        