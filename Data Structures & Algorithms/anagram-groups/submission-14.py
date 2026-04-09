class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for str_ in strs:
            arr = [0 for i in range(26)]
            for char in str_:
                arr[ord(char) - ord('a')]+=1


            key = "".join(str(arr))
            if key in dic:
                dic[key].append(str_)
            else:
                dic[key] = [str_]

        return list(dic.values())