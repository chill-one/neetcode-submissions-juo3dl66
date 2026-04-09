class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def get_count(string):
            count = [0] * 26

            for char in string:
                count[ord(char) - ord("a")] += 1

            return count

        dic = {}

        for str_ in strs:
            count = str(get_count(str_))
            if count in dic:
                dic[count].append(str_)
            else:
                dic[count] = [str_]


        return list(dic.values())

            