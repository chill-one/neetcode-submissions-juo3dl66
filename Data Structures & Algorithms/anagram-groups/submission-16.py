class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = defaultdict(list)

        
        def encode_to_anagram(s):
            arr = [0 for _ in range(26)]

            for char in s:
                key = ord(char) - ord('a')

                arr[key] += 1


            return "".join(str(arr))

        for s in strs:
            key = encode_to_anagram(s)
            anagram_list[key].append(s)


        return list(anagram_list.values())