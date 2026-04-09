class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(f"{len(string)}#{string}")

        res_string = "".join(res)
        return res_string

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        n = len(s)
        i = 0
        while(i < n):
            k = i
            while(s[k] != "#"):
                k+=1
            length = int(s[i:k])
            start = i + (k - i) + 1
            string = s[start : start + length]
            res.append(string)
            i = start + length

        return res

