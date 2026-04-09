class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for str_ in strs:
            word = f"{len(str_)}#{str_}"
            res.append(word)

        return "".join(res)
        
    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != '#':
                j+= 1
            len_ = int(s[i:j])
            word_ = s[j+1: j+len_+1]
            res.append(word_)
            i = j + len_ + 1
        return res
