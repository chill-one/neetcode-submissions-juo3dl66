class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        endIndex = {}
        for idx, char in enumerate(s):
            endIndex[char] = idx
        
        left = 0
        res = []
        seen = set()
        end = endIndex[s[left]]

        curr = []
        for right in range(len(s)):
            char = s[right]

            if right == end + 1:
                seen = set()
                res.append(len(curr))
                curr = []

            if char not in seen:
                end = max(end, endIndex[char])
            curr.append(char)
        res.append(len(curr))
        return res