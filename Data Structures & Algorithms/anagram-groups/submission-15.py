class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)

        def get_code(string):
            res = [0] * 26

            for char in string:
                res[ord(char) - ord('a')] += 1

            return str(res)


        for string in strs:
            code = get_code(string)
            anagram_group[code].append(string)


        return list(anagram_group.values())
                