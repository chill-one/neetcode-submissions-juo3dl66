class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for string in strs:
            res = [0 for i in range(26)]
            for char in string:
                res[ord(char) - ord("a")] += 1
            key = str(res)
            if key in dic:
                dic[key].append(string)
            else:
                dic[key] = [string]
        return list(dic.values())