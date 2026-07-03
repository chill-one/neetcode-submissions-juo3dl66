class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)

        for s in strings:
            l = []
            for idx in range(len(s) - 1):
                diff = (ord(s[idx]) - ord(s[idx + 1])) % 26
                l.append(str(abs(diff)))

            key = "".join(l)
            dic[key].append(s)

        return list(dic.values())
                
