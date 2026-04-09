class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        4#neet4#code4#love3#you

        number can be two digits
        """
        res = ""
        for string in strs:
            res += f'{len(string)}#{string}'
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0
        while(idx < len(s)):
            curr = idx
            while curr < len(s) and s[curr] != "#":
                curr+= 1
            str_length = s[idx : curr]
            length = int(str_length)

            start = idx + len(str_length) + 1
            string = s[start : start+length]
            res.append(string)
            idx += length + len(str_length) + 1

        return res
