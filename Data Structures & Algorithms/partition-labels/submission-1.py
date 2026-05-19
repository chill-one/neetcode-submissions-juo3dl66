class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        endIndex = {}
        for idx, char in enumerate(s):
            endIndex[char] = idx
        
        left = 0
        res = []
        end = endIndex[s[left]]
        for right in range(len(s)):
            char = s[right]
            end = max(end, endIndex[char])
            if right == end:
                res.append(right - left + 1)
                left = right + 1

        return res